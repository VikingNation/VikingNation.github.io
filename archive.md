---
layout: page
title: Archive
permalink: /archive/
---

{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}

{% for year in postsByYear %}
## {{ year.name }}

<ul>
  {% for post in year.items %}
    {% unless post.categories contains "mdc-emcomm-challenge" %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      <span class="post-date"> — {{ post.date | date: "%B %d" }}</span>
    </li>
    {% endunless %}
  {% endfor %}
</ul>

{% endfor %}
