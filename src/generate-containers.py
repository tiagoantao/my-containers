import sys
sys.path.append('.')
from containers import containers


def generate_container(container, machine, content):
    w = open(container, 'w')
    w.write('FROM %s\n' % machine)
    w.write('MAINTAINER Tiago Antao <tra@popgen.net>\n\n')
    for fname in content:
        w.write(open(fname).read())
        w.write('\n')
    w.close()

for name, content in containers.items():
    generate_container(name, "ubuntu:saucy", content)
