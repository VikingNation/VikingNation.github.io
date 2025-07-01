---
layout: page
title: VarAc Wednesday Event
permalink: /varacWed/
---

<h1>Latest Posts</h1>

<ul>
  {% assign filtered_posts = site.posts | where_exp: "post", "post.tags contains 'VarAC'" %}
  {% for post in filtered_posts %}
	<li>
	  <a href="{{ post.url }}">{{ post.title }}</a> - <em> {{ post.date | date: "%B %d, %Y" }}</em>
	</li>
  {% endfor %}

</ul>

<h3>Contact me</h3>
Jason Johnson &lt;<a href="mailto:k3jsj@arrl.net">k3jsj@arrl.net</a>&gt;
