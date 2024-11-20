import pytest
from main3 import sort_list

def test_sort1():
   assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_sort2():
   assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort3():
   assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]

def test_sort3():
   assert sort_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("numbers, expected", [
   ([7, 2, 5, 3], [2, 3, 5, 7]),
   ([10, -10, 0], [-10, 0, 10]),
   ([], []),
   ([1], [1])
])
def test_sort_list_parametrized(numbers, expected):
   assert sort_list(numbers) == expected


