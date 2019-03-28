from jinja2 import Template
template = Template(open("templates/main.html").read())

report_list = open('templates/rapor-eng.html').read()

for page in ('about', 'archive', 'index', 'contact'):
    contents = open('pages/%s.html' % page).read()
    template_contents = Template(contents)
    contents = template_contents.render(
        report_list=report_list)

    full_page = template.render(contents=contents)

    open('build/%s.html' % page, 'w').write(full_page)

