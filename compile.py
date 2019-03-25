from jinja2 import Template
template = Template(open("templates/main.html").read())

for page in ('about', 'archive', 'index', 'contact'):
    contents = open('pages/%s.html' % page).read()

    full_page = template.render(contents=contents)

    open('build/%s.html' % page, 'w').write(full_page)

