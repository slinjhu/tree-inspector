from tree_inspector.options import Options
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
           or type(obj) in [str, float, int, bool, bytes, complex]


class TreeNode(NamedTuple):
    name: str
    short_type: str
    full_type: str
    value: str = 'value not given'
    children: List['TreeNode'] = []

    @staticmethod
    def simple(name: str, obj: Any) -> 'TreeNode':
        short_type, full_type = get_type_name(obj)
        return TreeNode(name=name, short_type=short_type, full_type=full_type, value=str(obj))



class TreeBuilder:
    def __init__(self, options: Options = Options()):
        self.options = options

    def _node_list(self, name: str, obj: List[Any]) -> TreeNode:
        if len(obj) == 0:
            return TreeNode.simple(name, obj)
        else:
            elm_short_type, elm_full_type = get_type_name(obj[0])
            return TreeNode(name=name,
                            short_type=f'list[{elm_short_type}]',
                            full_type=f'list[{elm_full_type}]',
                            children=[self.node(str(i), v) for i, v in enumerate(obj)
                                      if i < self.options.max_elements_to_show_in_list],
                            value=f'Length {len(obj)}')

    def _node_dict(self, name: str, obj: Dict[Any, Any]) -> TreeNode:
        if len(obj) == 0:
            return TreeNode.simple(name, obj)
        else:
            children = []
            cnt = 0
            for k, v in obj.items():
                cnt += 1
                children.append(self.node(str(k), v))
                if cnt >= self.options.max_elements_to_show_in_dict:
                    break
            return TreeNode(name=name, short_type='dict', full_type='dict',
                            value=f'Size {len(obj)}', children=children)

    def _node_class(self, name: str, obj: Any) -> TreeNode:
        short_type, full_type = get_type_name(obj)
        if hasattr(obj, '__dict__'):
            children = [self.node(str(k), v) for k, v in obj.__dict__.items()]
            value = f'{len(obj.__dict__)} fields'
        else:
            children = []
            value = str(obj)

        return TreeNode(name=name, short_type=short_type, full_type=full_type, value=value, children=children)

    def _node_numpy_ndarray(self, name: str, obj: numpy.ndarray) -> TreeNode:
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
            return TreeNode.simple(name, obj)
        elif type(obj) == dict:
            return self._node_dict(name, obj)
        elif type(obj) == list:
            return self._node_list(name, obj)
        elif type(obj) == numpy.ndarray:
            return self._node_numpy_ndarray(name, obj)
        else:
            return self._node_class(name, obj)


