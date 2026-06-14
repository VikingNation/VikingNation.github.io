# K3JSJ Site Review — Jekyll Best Practices
*Generated: 2026-06-13*

---

## Summary

The site is built on the **Jekyll Now** theme (v1.2.0), a minimal blog-style starter. It is functional and publishes correctly to GitHub Pages. However, the theme is aging, and there are several bugs, deprecated settings, and missed opportunities worth addressing before investing in new content.

---

## 🔴 Bugs (Fix These First)

### 1. Broken links on the Software page
**File:** `software.md`  
All five software links use `{{ site.base-url }}` (with a hyphen), which is not a valid Jekyll variable. The correct variable is `{{ site.baseurl }}` (no hyphen). These links currently go nowhere.

```markdown
# Wrong
[Superstation]( {{ site.base-url }}/software/superstation)

# Correct
[Superstation]( {{ site.baseurl }}/software/superstation)
```

### 2. Deprecated `gems:` key in `_config.yml`
**File:** `_config.yml` line 77  
The `gems:` key was renamed to `plugins:` in Jekyll 3.5. While it still works via a compatibility shim, it generates a warning and will eventually stop working.

```yaml
# Wrong (deprecated)
gems:
  - jekyll-sitemap
  - jekyll-feed

# Correct
plugins:
  - jekyll-sitemap
  - jekyll-feed
```

### 3. Broken URL in wc-event post
**File:** `_posts/2026-06-13-wc-event.md` line 17  
The link is written as raw text inside Markdown link syntax, which won't render as a clickable link:
```markdown
# Wrong - shows the URL as text inside the brackets
Check out the [https://wc2026ses.org](https://wc2026ses.org)

# Correct
Check out the [WC2026 website](https://wc2026ses.org)
```

---

## 🟡 Improvements (High Value)

### 4. Google Analytics ID is hardcoded in two places
**File:** `_includes/analytics.html`  
The GA tracking ID `G-L2RPMWZVFJ` is hardcoded directly in `analytics.html`, but it is also stored in `_config.yml` under `google_analytics`. If you ever change the ID you would need to update both files. The include should use the config variable:

```html
<!-- Replace hardcoded ID with the config variable -->
<script async src="https://www.googletagmanager.com/gtag/js?id={{ site.google_analytics }}"></script>
...
gtag('config', '{{ site.google_analytics }}');
```

### 5. Duplicate analytics (Google Analytics + GoatCounter)
**File:** `_layouts/default.html` lines 18–20  
Both Google Analytics and GoatCounter are loaded on every page. While not a bug, it adds page weight and two separate tools tracking the same thing. Consider choosing one.

### 6. Add `jekyll-seo-tag` plugin
Currently the site has no Open Graph image, no Twitter card metadata, and limited SEO meta tags. The `jekyll-seo-tag` plugin handles all of this automatically.

**Gemfile:**
```ruby
gem "jekyll-seo-tag"
```
**`_config.yml` plugins section:**
```yaml
plugins:
  - jekyll-sitemap
  - jekyll-feed
  - jekyll-seo-tag
```
**`_includes/meta.html`** — add near the top:
```liquid
{% seo %}
```

### 7. Add post excerpts and descriptions
Only one post (Reefscape) has no `excerpt` or `description` in its frontmatter. The index page uses `post.excerpt` which falls back to the first paragraph. Adding an explicit `excerpt` to each post gives you control over what appears on the home page and in search results/social shares.

```yaml
---
layout: post
title: "2026 Lewis and Clark Trail on the Air"
excerpt: "Tips and progress notes for the annual LCTOTA special event."
categories: [hamradio, ses]
author: Jason Johnson (K3JSJ)
---
```

### 8. Contact info is duplicated across 4 files
Your email and contact info appears in `index.html`, `about.md`, `software.md`, and `MdcEmcomm.md`. Consider moving it into `_includes/contact.html` and replacing each instance with `{% include contact.html %}`.

---

## 🟢 Enhancements (Nice to Have)

### 9. Add post pagination
As the post count grows, the home page will list all posts on one page. Add `jekyll-paginate` to limit posts per page:

```yaml
# _config.yml
plugins:
  - jekyll-paginate
paginate: 10
paginate_path: "/page:num/"
```

### 10. Add post tags
Posts currently use `categories` (hamradio, ses, mdc-emcomm-challenge). Adding `tags` with more specific keywords (ft8, winlink, dmr, varac, etc.) would help visitors find related content and improve SEO.

```yaml
---
tags: [lctota, special-event, ft8, dx]
---
```

### 11. Remove dead Google+ code
**File:** `_includes/svg-icons.html` line 13 and `_config.yml` line 31  
Google+ was shut down in 2019. The `googleplus` footer link entry and its SVG icon can be safely removed.

### 12. Replace inline CSS with classes in posts
Several posts use inline `style="display: flex..."` for layouts (lctota-event.md, wc-event.md). This works but is hard to maintain. Consider adding a `.post-image-right` class to `style.scss` instead.

```css
/* style.scss */
.post-image-right {
  display: flex;
  align-items: center;
  gap: 20px;
}
```

### 13. Consider a modern theme upgrade
Jekyll Now is from ~2014. The 740px max container width is narrow by today's standards, and there is no dark mode support. Popular modern alternatives that are still simple to use:
- **[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)** — most popular Jekyll theme, very flexible
- **[Chirpy](https://chirpy.cotes.page/)** — modern look with dark mode, categories, tags, TOC
- **[Beautiful Jekyll](https://beautifuljekyll.com/)** — closest in spirit to Jekyll Now but actively maintained

A theme change is a significant effort but would give the site a modern look without rebuilding content.

### 14. Add a `_data` directory for structured content
Your software list in `software.md` is written as raw Markdown. Storing it in `_data/software.yml` and looping over it with Liquid would make it easier to add/update entries without editing HTML/Markdown structure.

---

## ✅ What's Already Done Well

- **Favicon** linked correctly (just added)
- **Custom domain** (`k3jsj.net`) configured via `CNAME`
- **Sitemap & RSS feed** via plugins
- **Category filtering** on home page (mdc-emcomm-challenge posts hidden) and MdcEmcomm page
- **`target="_blank"` with `rel="noopener noreferrer"`** used correctly on external links
- **`relative_url` filter** used correctly for local images in posts
- **GoatCounter** as a privacy-respecting analytics alternative
- **Buy Me a Coffee** integrated in both footer and About page
- **GnuPG key** linked in footer — nice touch for a technical audience

---

## Recommended Priority Order

| Priority | Item |
|---|---|
| 1 | Fix broken links in `software.md` (#1) |
| 2 | Fix `gems:` → `plugins:` in `_config.yml` (#2) |
| 3 | Fix broken URL in wc-event post (#3) |
| 4 | Fix hardcoded GA ID in analytics.html (#4) |
| 5 | Add `jekyll-seo-tag` (#6) |
| 6 | Remove Google+ references (#11) |
| 7 | Add pagination (#9) |
| 8 | Consider theme upgrade (#13) |
