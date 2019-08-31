# Inspector for Python objects

Tree Inspector is a package to inspect generic Python object interactively as a tree structure.

![Sample](https://slinjhu.github.io/tree-inspector/static/Sample.png)

**Try** the [sample html page](https://slinjhu.github.io/tree-inspector/static/Sample.html)

## Install
It is very simple to install Tree Inspector. Just do

```
pip install tree-inspector
```

## Usage
Using Tree Inspector is even simpler.

```python
from tree_inspector import dump_tree_to_file

dump_tree_to_file('Name', any_object, '/tmp/outfile.html')
```

## Configuring the tree view
To be continued