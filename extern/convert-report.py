
def count_spaces(line):
    n = 0
    for c in line:
        if c != ' ':
            break
        n += 1
    return n

def strip_number(line):
    line = line.lstrip('0123456789')
    line = line.lstrip('. ')
    return line

prev_indent = -1
for line in open('rapor-eng.txt'):
    indent = count_spaces(line)
    assert indent % 4 == 0
    indent = int(indent / 4)
    if indent < prev_indent:
        print(' ' * indent + '</ol>')
    if indent > prev_indent:
        print(' ' * prev_indent + '<ol>')
    prev_indent = indent
    line = line.strip(' \n')
    line = strip_number(line)
    print(' ' * indent + '<li>%s</li>' % line)
for i in range(prev_indent, 0, -1):
    print(' ' * (i - 1) + '</ol>')

