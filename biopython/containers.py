containers = {}
for number, dist, lib_dir, pg, pil in [
    ('2', 'vivid', 'python2.7', '9.3', ''),
    ('3', 'vivid', 'python3.4', '9.3', 'python3-pil')]:

    containers['Biopython%s' % number] = (
        ['Biopython-Basic', 'Biopython-Run'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number})
    containers['Biopython%s-Notebook' % number] = (
        ['Biopython-Basic', 'Biopython-Run', 'Biopython-nb'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number,
         'ver': '%s' % number})
    containers['Biopython%s-Tutorial' % number] = (
        ['Biopython-Basic', 'Biopython-Run', 'Biopython-basic-tutorial'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number,
         'ver': '%s' % number})
    containers['Biopython%s-Test' % number] = (
        ['Biopython-Basic', 'Biopython-BuildBot'],
        {'DIST': dist, 'python': 'python%s' % number, 'pg': pg,
         'pil': pil, 'python_dir': lib_dir, 'pip': 'pip%s' % number})
