# archivebox-index-generator
View your ArchiveBox index without the bloat, just a web browser

Copy generate_index_html.py into your ArchiveBox data folder (next to `index.sqlite3`), run `python3 generate_index_html.py`. You will now have a file called `index.html` which you can open in your web browser without having the Docker web server started.

## Installing

Requirements: Python 3000, Jinja2

```
pip3 install Jinja2
```

or:

```
apt install python3-jinja2
```

or

```
dnf install python3-jinja2
```

etc etc etc.
