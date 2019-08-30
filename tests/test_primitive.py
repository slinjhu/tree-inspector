from tree_inspector.tree_builder import TreeBuilder
import unittest
from enum import Enum, auto


class Dummy(Enum):
    A = auto()
    B = auto()


class TestPrimitiveTypes(unittest.TestCase):
    def check_node(self, x):
        node = TreeBuilder().node('var', x)
        self.assertEqual(node.short_type, x.__class__.__name__)
        self.assertEqual(len(node.children), 0)
        self.assertEqual(node.value, str(x))
        print(node)

    def test_multiple(self):
        self.check_node(18)
        self.check_node(1.23456)
        self.check_node('Some arbitrary string')
        self.check_node(b'a byte string')
        self.check_node(True)
        self.check_node(None)
        self.check_node(u'shelsl')
        self.check_node(Dummy.A)
        self.check_node(complex('1+2j'))


if __name__ == '__main__':
    unittest.main()
