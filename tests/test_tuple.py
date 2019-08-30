from tree_inspector.tree_builder import TreeBuilder
import unittest
from collections import namedtuple


NMTuple = namedtuple('NMTuple', ['aa', 'bb'])


class TestTuple(unittest.TestCase):
    def check_node(self, obj):
        builder = TreeBuilder()
        node = builder.node('', obj)
        self.assertEqual(len(node.children), 0)
        self.assertTrue(len(node.value) > 0)

    def test_tuple(self):
        self.check_node((1, 2, 3, 4))
        self.check_node(NMTuple(18, 'shels'))
        self.check_node(NMTuple(98.18911, False))


if __name__ == '__main__':
    unittest.main()
