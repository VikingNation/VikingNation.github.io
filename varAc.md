---
layout: page
title: VarAC Wednesday
permalink: /varacWed/
---

<h1>Documents</h1>
<ul>
<li><a href="https://www.varacwednesday.net/about.html">VarAC Wednesday Instructions</a></li>
<li><a href="https://www.varacwednesday.net/training.html#check-in-generator">Check-In Generator video walk-thru</a></li>
<li><a href="https://www.varacwednesday.net/training.html#top10-tips">VarAC Top 10 for New Users</a></li>
<li><a href="https://www.varacwednesday.net/ttraining.html#voice-announcements">Voice Announcement Setup</a></li>
<li><a href="https://www.varacwednesday.net/training.html#pskreporter">PSKReporter for VarAC</a></li>
<li><a href="https://www.varacwednesday.net/ttraining.html#minimize-disconnects">Minimizing VarAC disconnects</a></li>
<li><a href="https://www.varacwednesday.net/training.html#vara-meter">Setting VARA HF VU Meter</a></li> 
</ul>
<h1>Video Tutorials</h1>
<ul>
<li><a href="https://youtu.be/Vu3j_ioLzhQ">VarAC Wednesday Check-in generator</a></li>
<li><a href="https://youtu.be/ezDjLdeTgMA">Using VarAC canned messages</a></li>
</ul>

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
