import unittest

import uuid

from tree_inspector.tree_builder import TreeBuilder


class TestClass(unittest.TestCase):
    def test_class_without_dict(self):
        obj = (4, 8)
        self.assertFalse(hasattr(obj, '__dict__'))

        node = TreeBuilder().node('dummy', obj)
        self.assertEqual(len(node.children), 0)

    def test_regular_class(self):
        obj = RegularClass()
        node = TreeBuilder().node('obj', obj)
        self.assertEqual(len(node.children), 1)

        obj = obj.add_fields()
        node2 = TreeBuilder().node('obj', obj)
        self.assertEqual(len(node2.children), 2)

    def test_others(self):
        self.check_node(uuid.uuid4())
        self.check_node(uuid.UUID)
        self.check_node(int)
        self.check_node(type)
        self.check_node(range(18))
        self.check_node(self)

    def check_node(self, obj):
        builder = TreeBuilder()
        node = builder.node('', obj)
        self.assertIsNotNone(node)
        print(node)


class RegularClass:
    def __init__(self):
        self.dummy = 7

    def add_fields(self):
        self.extra = 'random string'
        return self


if __name__ == '__main__':
    unittest.main()
