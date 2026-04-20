---
layout: page
title: MDC Emcomm Challenge
permalink: /MdcEmcomm/
---

<h1>Purpose</h1>
<p>
The ARRL MDC section runs a monthly digital challenge that provides operators the opportunity to gain experience usiing digital modes. The monthly digital challange is organized by Bill Smith (N3XL). Questions about the monthly ARRL MDC section digital challange should be directed to Bill via his email on <a href="https://www.qrz.com/db/N3XL" target="_blank" rel="noopener">N3XL's QRZ page</a>.
</p>

<h1>Reference documents</h1>
<p>
<ul>
<li><a href="https://docs.google.com/presentation/d/1C4O1uOplDYncrr02BLRV4fmbCrE2LAe4/preview" target="_blank" rel="noopener">Winlink Global Email Service</a></li>
<li><a href="https://docs.google.com/document/d/1nCoICW15oq32yeY1fZoPngH8ss2N5-ZYZ-ulbzcTLGk/preview" target="_blank" rel="noopener">How to install RMS Express (Winlink)</a></li>
<li><a href="https://docs.google.com/document/d/1-mq9O9glnC9-etMk7ryxIVYt6rXENx8HanUkXzr8lhk/preview" target="_blank" rel="noopener">Winlink Tips</a></li>
<li><a href="https://docs.google.com/document/d/1RcKPAFrTWPzs_3MdejcuJG_fm9wbW5k7hh7g0kqPn84/preview" target="_blank" rel="noopener">VarAC Tips</a></li>
<li><a href="https://docs.google.com/document/d/1w57SGGP2Hy2i62fwv0LSo-cQ4r6ECav2aU4jBzOj_jw/preview" target="_blank" rel="noopener">Fldigi Tips</a></li>
<li><a href="https://docs.google.com/document/d/1JfXeFBfRHxLt-Q_q2krs-LVZbZvldtAM/preview" target="_blank" rel="noopener">Tips in brevity in Emergency Communications</a></li>
</ul>
</p>

<h2>MDC Digital EMCOMM Challenge – Latest Posts</h2>

<ul>
{% for post in site.posts %}
  {% if post.categories contains "mdc-emcomm-challenge" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
    </li>
  {% endif %}
{% endfor %}
</ul>

<h3>Contact me</h3>
Jason Johnson &lt;<a href="mailto:k3jsj@arrl.net">k3jsj@arrl.net</a>&gt;
