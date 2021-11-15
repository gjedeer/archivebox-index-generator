#!/usr/bin/python3

import datetime
import glob
import jinja2
import json
import os.path

template = """
<html>
<body>
<h1>Generated: {{ date }}</h1>
{% for s in found_sites %}
<div class="oneentry" style="clear: both">
<img style="float: left; margin: 10px; max-width: 10%" src="{{ s.dir }}/screenshot.png">
<h3>{{ s.data.title }}</h3>
<p><a href="{{ s.dir }}/index.html">Index</a> | <a href="{{ s.dir }}/output.pdf">PDF</a> | <a href="{{ s.dir }}/output.html">HTML</a> | Original: {{ s.data.url }}</p>
</div>
{% endfor %}
</body>
</html>
"""

if __name__ == '__main__':
    found_sites = []

    for index_path in glob.glob('archive/*/index.json'):
        with open(index_path) as f:
            data = json.load(f)
            found_sites.append({
                'file': index_path, 
                'dir': os.path.dirname(index_path), 
                'data': data
            })
    ctx = {
        'date': datetime.datetime.now(),
        'found_sites': found_sites,
    }
    template = jinja2.Template(template)
    html = template.render(**ctx)
    with open('index.html', 'w') as f:
        f.write(html)


