from tree_inspector import dump_tree_to_file
import unittest
import os
import uuid
import numpy


class TestFile(unittest.TestCase):
    def test_write(self):
        dt = numpy.dtype([('name', numpy.unicode_, 16), ('grades', numpy.float64, (2,))])
        obj = {
            'a': [1, 2, 3, 4, 5, 6, 7, 9],
            'b': uuid.uuid4(),
            'plain_numpy_array': numpy.array([range(10), range(10)]),
            'fancy_numpy_array': numpy.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt),
            'some_tuple': ('Hello', 'World', 2019)
        }
        outfile = f'/tmp/{uuid.uuid4()}.html'

        dump_tree_to_file(obj, outfile)
        self.assertTrue(os.path.exists(outfile))


if __name__ == '__main__':
    unittest.main()
