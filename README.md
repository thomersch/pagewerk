# PageWerk

Pagewerk is a tiny wrapper around jinja2, that allows you to easily put your content pages into a template.

## How to run PageWerk

	./pagewerk.py

It will take all files from `pages` directory, wrap the template from `template.tpl` (there is an example in `template.example.tpl`) around and put the results with the same file name into the `pub` directory.

You can automatically rerender on file changes with fswatch:

	fswatch -o pages/ | xargs -n1 pagewerk.py

## Configuration

There is no configuration file. If you don't like how Pagewerk behaves, just change the source - it is very short and should be too hard to understand.
