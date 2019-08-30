from tree_inspector.tree_builder import TreeBuilder, Options
import unittest


class TestTuple(unittest.TestCase):
    def test_empty(self):
        builder = TreeBuilder()
        self.assertIsNotNone(builder.node('', {}))
        self.assertIsNotNone(builder.node('', {'a': {}}))

    def test_truncation(self):
        xx = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
        yy = {'a': 'a'}
        option = Options(max_elements_to_show_in_dict=3)
        builder = TreeBuilder(option)
        self.assertEqual(len(builder.node('', xx).children), 3)
        self.assertEqual(len(builder.node('', yy).children), 1)

    def test_nested(self):
        builder = TreeBuilder()
        nd = builder.node('', {'a': {'b': 'b'}})
        print(nd)
        self.assertEqual(len(nd.children), 1)
        self.assertEqual(len(nd.children[0].children), 1)


if __name__ == '__main__':
    unittest.main()
