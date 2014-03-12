containers = {
    'Biopython': ['Biopython-Basic', 'Biopython-Run'],
    'Biopython-Test': ['Biopython-Basic', 'Biopython-BuildBot'],
}


def generate_container(container, machine, content):
    w = open(container, 'w')
    for fname in content:
        w.write(open(fname).read())
    w.close()

for name, content in containers.items():
    generate_container(name, "ubuntu:saucy", content)
