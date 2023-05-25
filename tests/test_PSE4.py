import pytest
from PSEs.PSE4_palindrome import palindrome

def test_case_insensitive():
    s = "Noon"
    palindrome(s)
    assert palindrome(s) == True

def test_ignore_spaces():
    s = "was it a car or a cat i saw"
    palindrome(s)
    assert palindrome(s) == True

def test_ignore_punctuation():
    s = "A man, a plan, a canal, Panama!"
    assert palindrome(s) == True

def test_empty_string():
    s = ""
    try:
        palindrome(s)
    except TypeError as err:
        assert str(err) == "Invalid input"
    else:
        assert False, "Expected TypeError"

def test_not_palindrome():
    s = "hello"
    assert palindrome(s) == False

def test_palindrome_with_odd_length():
    s = "racecar"
    assert palindrome(s) == True

def test_palindrome_with_even_length():
    s = "deed"
    assert palindrome(s) == True
