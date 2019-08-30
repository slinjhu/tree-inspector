from tree_inspector.tree_builder import dump_tree_to_file
from dataclasses import dataclass
from enum import Enum, auto
import numpy


class Fruit(Enum):
    APPLE = auto()
    PEAR = auto()


@dataclass
class Coordinate:
    x: float = 0
    y: float = 0


class SampleClass:
    def __init__(self):
        self.string_field = 'Some string value'
        self.coordinates = [Coordinate(), Coordinate()]
        self.a_array = numpy.array(range(1, 30))
        self.a_ndarray = numpy.ones([3, 5, 6])
        self.nonsense = None
        self.a_enum_field = Fruit.APPLE
        self.a_dict_field = {
            'balabala': "A message",
            'an array': [111, 222, 333],
            555: 'Interesting. Python dict can have keys of different types'
        }



if __name__ == '__main__':
    sample = SampleClass()
    dump_tree_to_file('sample', sample, 'out.html')
