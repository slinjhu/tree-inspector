import unittest
from collections import namedtuple

from tree_inspector.tree_builder import TreeBuilder


class TestTuple(unittest.TestCase):

    def test_simple_tuple(self):
        obj = (1, 2, 3, 4)
        builder = TreeBuilder()
        node = builder.node('', obj)
        self.assertEqual(len(node.children), 0)
        self.assertTrue(len(node.value) > 0)

    def test_namedtuple(self):
        NMTuple = namedtuple('NMTuple', ['aa', 'bb'])
        obj = NMTuple(18, 'shels')
        builder = TreeBuilder()
        node = builder.node('', obj)
        self.assertEqual(len(node.children), 0)
        self.assertTrue(len(node.value) > 0)


if __name__ == '__main__':
    unittest.main()
