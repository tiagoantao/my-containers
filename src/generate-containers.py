import sys
sys.path.append('.')
from containers import containers


def generate_container(container, templates, vars):
    w = open(container, 'w')
    w.write('FROM ubuntu:%s\n' % vars['DIST'])
    w.write('MAINTAINER Tiago Antao <tra@popgen.net>\n\n')
    w.write('ENV DEBIAN_FRONTEND noninteractive\n')
    for fname in templates:
        temp_text = open(fname).read()
        for var_name, var_replace in vars.items():
            temp_text = temp_text.replace('<' + var_name + '>', var_replace)
        w.write(temp_text)
        w.write('\n')
    w.close()

for name, content in containers.items():
    templates, vars = content
    generate_container(name, templates, vars)
