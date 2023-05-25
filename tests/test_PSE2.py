import pytest
from PSEs.PSE2_adagrams import score


def test_duplicate_letters_returns_score_correctly():
    word = "AAA"
    output = score(word)
    assert output == 3 

def test_empty_input_returns_zero_score():
    word = ""
    output = score(word)
    assert output == 0

def test_score_with_mixed_case_input():
    word = "GoOD"
    output = score(word)
    assert output == 6

def test_score_with_special_characters():
    word = "C@t"
    output = score(word)
    assert output == 4

def test_score_with_whitespace():
    word = "Open AI"
    output = score(word)
    assert output == 8

def test_score_with_all_letters():
    word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = score(word)
    assert output == 87

def test_score_with_nonexistent_letters():
    word = "XYZ123"
    output = score(word)
    assert output == 22
