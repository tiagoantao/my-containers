A set of docker containers that might be useful to others
=========================================================


The containers are divided in directories, currently only a biopython
directory exists.

As some containers share the specification, there is a set of templates to
help generate the final containers

Each directory has a set of container templates. The file
containers.py specifies how to generate the containers proper, for example:

```python
containers = {
    'Biopython': ['Biopython-Basic', 'Biopython-Run'],
    'Biopython-Test': ['Biopython-Basic', 'Biopython-BuildBot'],
}
```

Two containers will be generated:

1. The first is composed from template Biopython-Basic followed by
   Biopython-Run. It will be called Biopython.

2. The second is composed from template Biopython-Basic followed by
   Biopython-BuildBot. It will be called Bioython-Test.


To generate the containers, you can do

1. cd to your directory of interest (e.g. bioython)

2. python ..src/generate-containers.py

