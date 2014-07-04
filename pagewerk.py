#!/usr/bin/env python3

import os
import jinja2

try:
	from bs4 import BeautifulSoup
	SOUP_AVAILABLE = True
except ImportError:
	print("Page title detection is not available, please install BeautifulSoup to enable the feature: pip install beautifulsoup4")
	SOUP_AVAILABLE = False

INPUT_PAGES = "pages"
OUTPUT_PATH = "pub"


def template_page(page_name, page_content, page_title, template):
	with open(os.path.join(OUTPUT_PATH, page_name), "w+") as html_page:
		html_page.write(template.render({"content": page_content, "title": page_title}))


def get_page_title(page_content):
	soup = BeautifulSoup(page_content)
	try:
		return soup.h1.text
	except AttributeError:
		return None


def render_pages(path, template_engine):
	template = template_engine.get_template("template.tpl")
	pages_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	for page_path in pages_paths:
		with open(page_path, "r") as f:
			page_content = f.read()

			if SOUP_AVAILABLE:
				page_title = get_page_title(page_content)
			else:
				page_title = None

			page_name = os.path.basename(page_path)
			template_page(page_name, page_content, page_title, template)


def main():
	if not os.path.exists(OUTPUT_PATH):
		os.mkdir(OUTPUT_PATH)
	template_engine = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
	render_pages(INPUT_PAGES, template_engine)


if __name__ == "__main__":
	main()