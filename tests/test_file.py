from tree_inspector import dump_tree_to_file
import unittest
import os
import uuid


class TestFile(unittest.TestCase):
    def test_write(self):
        obj = {'a': [], 'b': {}}
        outfile = f'/tmp/{uuid.uuid4()}.html'

        dump_tree_to_file(obj, outfile)
        self.assertTrue(os.path.exists(outfile))


if __name__ == '__main__':
    unittest.main()
