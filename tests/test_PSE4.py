import pytest
from PSEs.PSE4_palindrome import palindrome

def test_case_insensitive():
    # ^rename with meaningful test name
    # and complete test implementation below
    pass
    # arrange
    s = "Noon"

    # act
    palindrome(s)

    # assert
    assert palindrome(s) == True

def test_ignore_spaces():
    # ^rename with meaningful test name
    # and complete test implementation below
    pass
    
    # arrange
    s = "was it a car or a cat i saw"

    # act
    palindrome(s)

    # assert
    assert palindrome(s) == True