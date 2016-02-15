import twoIndices
import random
import sys


def setup_test():
    # Generate an array of random numbers
    array_out = []
    array_size = 100
    uniqueness_set = set()
    for index in range(array_size):
        safety = 0
        new_int = random.randint(0, sys.maxsize)
        while new_int not in uniqueness_set:
            new_int = random.randint(0, sys.maxsize)
            safety += 1
            assert(safety < 100)
        array_out.append(new_int)
        uniqueness_set.add(new_int)

    return array_out

def test_good_setup():
    integer_array = setup_test()
    first_index = 1
    second_index = 2
    target = integer_array[first_index] + integer_array[second_index]
    test_array = twoIndices(integer_array, target)

    assert(first_index == test_array[1])
    assert(second_index == test_array[2])