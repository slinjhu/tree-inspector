from tree_inspector.tree_builder import TreeBuilder, Options
import unittest


class TestTuple(unittest.TestCase):
    def test_empty(self):
        builder = TreeBuilder()
        self.assertIsNotNone(builder.node('', []))
        self.assertIsNotNone(builder.node('', [[[]]]))
        self.assertIsNotNone(builder.node('', [[]]))
        self.assertIsNotNone(builder.node('', [[], []]))

    def test_truncation(self):
        xx = [1, 2, 3, 4, 5]
        yy = [1, 2]
        option = Options(max_elements_to_show_in_list=3)
        builder = TreeBuilder(option)
        self.assertEqual(len(builder.node('', xx).children), 3)
        self.assertEqual(len(builder.node('', yy).children), 2)

    def test_nested(self):
        builder = TreeBuilder()
        nd = builder.node('', [[1, 2], [3, 4, 5]])
        self.assertEqual(len(nd.children), 2)


if __name__ == '__main__':
    unittest.main()
