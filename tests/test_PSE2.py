import pytest
from PSEs.PSE2_adagrams import score


def test_duplicate_letters_returns_score_correctly():
    # ^rename with meaningful test name
    # and complete test implementation below
    pass
    # arrange
    word = "AAA"

    # act
    output = score(word)

    # assert
    assert output == 3 

def test_empty_input_returns_zero_score():
    # ^rename with meaningful test name
    # and complete test implementation below
    pass
    
    # arrange
    word = ""
    
    # act
    output = score(word)
    
    # assert
    
    assert output == 0