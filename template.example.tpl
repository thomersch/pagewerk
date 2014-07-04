<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" href="style.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
	<title>Page {{ title }}</title>
</head>

<body>
	<header>
		<div id="signet">
		</div>
	</header>
	<section id="maincontent">
		{% block content %}
			{{ content }}
		{% endblock %}
	</section>

	{% block extjs %}
	{% endblock %}
</body>
</html>