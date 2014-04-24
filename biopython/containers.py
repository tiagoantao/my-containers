containers = {}
for number, dist, lib_dir, pg in [('', 'saucy', 'python2.7', '9.1'),
                              ('3', 'trusty', 'python3.4', '9.3')]:
    containers['Biopython%s' % number] = (
        ['Biopython-Basic', 'Biopython-Run'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'python_dir': lib_dir, 'pip': 'pip%s' % number})
    containers['Biopython%s-Test' % number] = (
        ['Biopython-Basic', 'Biopython-BuildBot'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'python_dir': lib_dir, 'pip': 'pip%s' % number})
