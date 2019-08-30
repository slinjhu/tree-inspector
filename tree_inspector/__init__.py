import os
from tree_inspector.tree_builder import Options, TreeBuilder
from jinja2 import Template


def dump_tree_to_file(obj, outfile, name='object', options: Options = Options()):
    pwd = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(pwd, 'template.html')
    tree_builder = TreeBuilder(options)
    node = tree_builder.node(name, obj)
    with open(template_file, 'r') as tf:
        html = Template(tf.read()).render(name=name, node=node)
        with open(outfile, 'w') as outf:
            outf.write(html)

