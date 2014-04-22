import sys
sys.path.append('.')
from containers import containers


def generate_container(container, templates, vars):
    w = open(container, 'w')
    w.write('FROM %s\n' % vars['DIST'])
    w.write('MAINTAINER Tiago Antao <tra@popgen.net>\n\n')
    for fname in templates:
        # should apply other vars
        w.write(open(fname).read())
        w.write('\n')
    w.close()

for name, content in containers.items():
    templates, vars = content
    generate_container(name, templates, vars)
