from jinja2 import Template
from options import Options
from typing import Any, List, NamedTuple, Dict
import numpy
import enum


def get_type_name(o):
    short = o.__class__.__name__
    module = o.__class__.__module__
    return short, module + '.' + short


def is_primitive(obj: Any) -> bool:
    return obj is None \
           or issubclass(type(obj), enum.Enum) \
           or type(obj) in [str, float, int, bool, bytes]


class TreeNode(NamedTuple):
    name: str
    short_type: str
    full_type: str
    value: str = 'value not given'
    children: List['TreeNode'] = []


class TreeBuilder:
    def __init__(self, options: Options = Options()):
        self.options = options

    def node_primitive(self, name, obj):
        short_type, full_type = get_type_name(obj)
        return TreeNode(name=name, short_type=short_type, full_type=full_type, value=str(obj))

    def node_list(self, name: str, obj: List[Any]) -> TreeNode:
        if len(obj) == 0:
            return TreeNode(name=name, short_type='List', full_type='List', value='Empty List')
        else:
            elm_short_type, elm_full_type = get_type_name(obj[0])
            return TreeNode(name=name,
                            short_type=f'List[{elm_short_type}]',
                            full_type=f'List[{elm_full_type}]',
                            children=[self.node(str(i), v) for i, v in enumerate(obj)
                                      if i < self.options.max_elements_to_show_in_list],
                            value=f'Length {len(obj)}')

    def node_dict(self, name: str, obj: Dict[Any, Any]) -> TreeNode:
        if len(obj) == 0:
            return TreeNode(name=name, short_type='Dict', full_type='Dict', value='Empty Dict')
        else:
            children = []
            cnt = 0
            for k, v in obj.items():
                cnt += 1
                children.append(self.node(str(k), v))
                if cnt >= self.options.max_elements_to_show_in_dict:
                    break
            return TreeNode(name=name, short_type='Dict', full_type='Dict',
                            value=f'Size {len(obj)}', children=children)

    def node_class(self, name: str, obj: Any) -> TreeNode:
        short_type, full_type = get_type_name(obj)
        if hasattr(obj, '__dict__'):
            children = [self.node(str(k), v) for k, v in obj.__dict__.items()]
            value = f'{len(obj.__dict__)} fields'
        else:
            children = []
            value = str(obj)

        return TreeNode(name=name, short_type=short_type, full_type=full_type, value=value, children=children)

    def node_numpy_ndarray(self, name: str, obj: numpy.ndarray) -> TreeNode:
        if obj.size < self.options.max_size_to_show_in_numpy_ndarray:
            value = str(obj)
        else:
            value = f'Max: {obj.max()}\nMin: {obj.min()}\nMean: {obj.mean()}'
        return TreeNode(name=name,
                        short_type=f'ndarray[{obj.dtype}], Shape {obj.shape}',
                        full_type=f'numpy.ndarray[{obj.dtype}], Shape {obj.shape}',
                        value=value)

    def node(self, name: str, obj: Any) -> TreeNode:
        """
        Render a Python object as html.
        :param obj: The object to be rendered; Could be of any type
        :param name: variable name or any string label for the given object
        :return: html string
        """
        if is_primitive(obj):
            return self.node_primitive(name, obj)
        elif type(obj) == dict:
            return self.node_dict(name, obj)
        elif type(obj) == list:
            return self.node_list(name, obj)
        elif type(obj) == numpy.ndarray:
            return self.node_numpy_ndarray(name, obj)
        else:
            return self.node_class(name, obj)


def dump_tree(name, obj, outfile, options: Options = Options()):
    template_file = 'template.html'
    tree_builder = TreeBuilder(options)
    node = tree_builder.node(name, obj)
    with open(template_file, 'r') as tf:
        html = Template(tf.read()).render(name=name, node=node)
        with open(outfile, 'w') as outf:
            outf.write(html)

