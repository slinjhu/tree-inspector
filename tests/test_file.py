from tree_inspector import dump_tree_to_file
import unittest
import os
import uuid
import numpy


class SampleClass:
    def __init__(self):
        dt = numpy.dtype([('name', numpy.unicode_, 16), ('grades', numpy.float64, (2,))])
        self.a_array = [1, 2, 3, 4, 5, 6, 7, 9]
        self.id = uuid.uuid4()
        self.plain_numpy_array = numpy.array([range(10), range(10)])
        self.fancy_numpy_array = numpy.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
        self.some_tuple = ('Hello', 'World', 2019)
        self.some_dict = {
            'one': 1,
            'two': 2
        }


class TestFile(unittest.TestCase):
    def test_write(self):

        obj = SampleClass()
        outfile = f'/tmp/{uuid.uuid4()}.html'

        dump_tree_to_file(obj, outfile)
        self.assertTrue(os.path.exists(outfile))
        print(outfile)


if __name__ == '__main__':
    unittest.main()
