containers = {}
for number, dist, lib_dir in [('', 'saucy', 'python2.7'),
                              ('3', 'trusty', 'python3.4')]:
    containers['Biopython%s' % number] = (
        ['Biopython-Basic', 'Biopython-Run'],
        {'DIST': dist, 'python': 'python%s' % number,
         'python_dir': lib_dir})
    containers['Biopython%s-Test' % number] = (
        ['Biopython-Basic', 'Biopython-BuildBot'],
        {'DIST': dist, 'python': 'python%s' % number,
         'python_dir': lib_dir})
