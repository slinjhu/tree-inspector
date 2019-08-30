from tree_inspector.tree_builder import TreeBuilder, Options
import unittest
import numpy



class TestClass(unittest.TestCase):

    def test_2d_array(self):
        builder = TreeBuilder(Options(max_elements_to_show_in_list=3))
        obj = numpy.array([range(1, 10), range(1, 10)])
        node = builder.node('', obj)
        self.assertEqual(len(node.children), 2)
        self.assertEqual(len(node.children[0].children), 3)

    def test_flexible_type(self):
        dt = numpy.dtype([('name', numpy.unicode_, 16), ('grades', numpy.float64, (2,))])
        x = numpy.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
        node = TreeBuilder().node('', x)
        self.assertEqual(len(node.children), 2)


if __name__ == '__main__':
    unittest.main()

