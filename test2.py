import pytest
from main2 import is_palindrome

def test_is_palindrome_true():
   assert is_palindrome("madam") == True

def test_is_palindrome_false():
   assert is_palindrome("hello") == False

@pytest.mark.parametrize("s, expected", [
   ("level", True),
   ("python", False),
   ("racecar", True),
   ("", True),
   ("a", True),
])
def test_is_palindrome_parametrized(s, expected):
   assert is_palindrome(s) == expected
