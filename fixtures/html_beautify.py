from bs4 import BeautifulSoup
html = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<html>
<head>
<title>
{% block title %}
Page title
{% endblock %}
</title>
<link rel="stylesheet" href="/static/bootstrap/css/bootstrap.css"/>
      <link rel="icon" href="/static/img/favicon.ico"type="image/x-ico"/>
      
<style type="text/css">
<!--
.contents{
  width: 70%;
        float: right;
}
.sidebar{
   width: 25%;
         float: right;
}
-->
</style>

</head>
<body>

<div class="contents">

{% block contents %}

asdf
{% endblock %}
</div>

<div class="sidebar">
{% block sidebar %}
<h3>Meta</h3>
<ul>
<li>
<a href="/create/"> Create new Poll</a>

</li>
</ul>

<h3>Recent Polls</h3>
<ul>
{% for poll in recents %}
<li>
<a href="{{poll.get_absolute_url}}">{{poll.question}}</a>

</li>
{% endfor %}
</ul>
{% endblock %}
</div>

</body>
</html>
"""
page = BeautifulSoup(html_doc)
page.pretify()
