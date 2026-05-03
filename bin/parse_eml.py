import email
import re
import argparse
from email import policy
from email.parser import BytesParser
from datetime import datetime
import os

SECTION_HEADERS = [
    "SCOPE",
    "PURPOSE",
    "PLANNING",
    "EXECUTION",
    "EXAMPLE OF A LOCAL Wx FORECAST",
    "FLMSG TIPS",
    "NOTES",
    "CHALLENGE CREDIT",
    "TASK 1",
    "TASK 2",
    "TASK 3"
]

def load_eml(path):
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)
    return msg

def extract_plaintext(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(errors="replace")
    else:
        return msg.get_payload(decode=True).decode(errors="replace")
    return ""

def normalize_header(text):
    return text.strip().rstrip(":").upper()

def split_sections(body_text):
    sections = {}
    pattern = r"(?P<header>" + "|".join([re.escape(h) for h in SECTION_HEADERS]) + r")\s*:?"
    matches = list(re.finditer(pattern, body_text, flags=re.IGNORECASE))

    if not matches:
        return sections

    for i, match in enumerate(matches):
        header = normalize_header(match.group("header"))
        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(body_text)

        content = body_text[start:end].strip()
        sections[header] = content

    return sections

def extract_metadata(msg):
    return {
        "subject": msg.get("Subject", "").strip(),
        "date": msg.get("Date", "").strip(),
        "from": msg.get("From", "").strip(),
        "to": msg.get("To", "").strip()
    }

def parse_eml_to_sections(path):
    msg = load_eml(path)
    body = extract_plaintext(msg)
    sections = split_sections(body)
    metadata = extract_metadata(msg)

    return {
        "metadata": metadata,
        "sections": sections,
        "raw_body": body
    }


def generate_markdown(data):
    meta = data["metadata"]
    sections = data["sections"]

    # Convert email date → YYYY-MM-DD
    try:
        dt = datetime.strptime(meta["date"], "%a, %d %b %Y %H:%M:%S %z")
        date_str = dt.strftime("%Y-%m-%d")
    except:
        date_str = "2026-01-01"

    # Clean title
    title = meta["subject"].replace("ANNOUNCEMENT:", "").strip()

    # Create a slug for permalink
    slug = title.lower().replace(" ", "-").replace("–", "-").replace("—", "-")
    slug = re.sub(r"[^a-z0-9\-]", "", slug)

    md = []
    md.append(f"---")
    md.append(f'layout: post')
    md.append(f'title: "{title}"')
    md.append(f"date: {date_str}")
    md.append(f"categories: [mdc-emcomm-challenge]")
    md.append(f'author: "MDCWINLINK-1"')

    # UNIQUE PERMALINK FIX
    md.append(f'permalink: /mdc-emcomm-challenge/{date_str}-{slug}/')

    md.append(f"tags: [winlink, varac, fldigi, emcomm, mdc-section]")
    md.append(f"---\n")

    # md.append(f"# {title}\n")
    md.append(f"**Source:** {meta['from']}\n")

    for header, content in sections.items():
        md.append(f"\n## {header.title()}\n")
        md.append(content + "\n")

    return "\n".join(md)

def save_markdown(md_text, date_str, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{date_str}-mdc-emcomm-challenge.md"
    path = os.path.join(output_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(md_text)

    return path

def main():
    parser = argparse.ArgumentParser(description="Parse an .eml file and generate a Jekyll markdown announcement.")
    parser.add_argument("eml_file", help="Path to the .eml file to parse")
    args = parser.parse_args()

    data = parse_eml_to_sections(args.eml_file)
    meta_date = data["metadata"]["date"]

    try:
        dt = datetime.strptime(meta_date, "%a, %d %b %Y %H:%M:%S %z")
        date_str = dt.strftime("%Y-%m-%d")
    except:
        date_str = "2026-01-01"

    md_text = generate_markdown(data)
    output_path = save_markdown(md_text, date_str)

    print(f"\nMarkdown file generated:\n{output_path}\n")

if __name__ == "__main__":
    main()

