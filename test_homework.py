import pytest
from main_homework import count_vowels

def test_count_vowels1():
   assert count_vowels('abracadabra') == 5

def test_count_vowels2():
   assert count_vowels('aeiouy') == 6

def test_count_vowels3():
   assert count_vowels('frtpr') == 0

def test_count_vowels3():
   assert count_vowels('aeiouyAEIOUY') == 12

@pytest.mark.parametrize("str, expected", [
   ('abracadabra', 5),
   ('aeiouy', 6),
   ('frtpr', 0),
   ('aeiouyAEIOUY', 12),
   ('', 0)
])
def test_count_vowels_parametrized(str, expected):
   assert count_vowels(str) == expected


