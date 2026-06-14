---
layout: page
title: VarAC Wednesday
permalink: /varacWed/
---

## Overview
<a href="https://www.varacwednesday.net" target="_blank">VarAC Wednesday</a> is a weekly amateur radio digital net where users check-in by sending a message via a station providing EMAIL gateway service. We offer a number of <a href="https://www.varacwednesday.net/awards" target="_blank">Awards</a> to recognize special events and operator achievements. We also sponsor the <a href="https://www.varacwednesday.net/superstation" target="_blank">SUPERSTATION</a> game and contest. 

## Latest News
Check out our announcements on the <a href="https://www.varacwednesday.net/home/news" target="_blank">VarAC News page</a>

## Weekly Results
See our website for <a href="https://www.varacwednesday.net/varac-wednesday/results" target="_blank">Weekly Results</a> as well as our <a href="https://www.varacwednesday.net/varac-wednesday/map" target="_blank">Weekly Check-in map</a>


## Historic Results
Historic weekly results (May 7 2025 - July 23 2025) are posted here.  See our VarAC website for current news.

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
