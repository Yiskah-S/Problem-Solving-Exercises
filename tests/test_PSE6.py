import pytest
from PSEs.PSE6_merging_sorted_lists import merge_lists

def test_both_lists_are_empty():
    list1 = []
    list2 = []

    try:
        result = merge_lists(list1, list2)
    except ValueError as err:
        assert str(err) == "Both lists are empty"
    else:
        assert False, "Expected ValueError wasn't raised"

def test_list_contains_non_numerals():
    list1 = [2, 1, 3]
    list2 = ["invalid"]

    try:
        result = merge_lists(list1, list2)
    except TypeError as err:
        assert str(err) == "Invalid input in list"
    else:
        assert False, "Expected TypeError wasn't raised"

def test_returns_sorted_list_if_one_is_empty_at_start():
    list1 = [1, 2, 3]
    list2 = []

    result = merge_lists(list1, list2)

    assert result == [1, 2, 3]

def test_input_not_list_raises_error():
    list1 = "invalid"
    list2 = 3

    try:
        result = merge_lists(list1, list2)
    except TypeError as err:
        assert str(err) == "Invalid input, lists must be a list"
    else:
        assert False, "Expected TypeError wasn't raised"

def test_lists_same_lenght_return_correctly():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    result = merge_lists(list1, list2)

    assert result == [1, 2, 3, 4, 5, 6]

def test_lists_different_lenght_return_correctly():
    list1 = [1, 2, 3]
    list2 = [4]

    result = merge_lists(list1, list2)

    assert result == [1, 2, 3, 4]

def test_negative_nums_return_correctly():
    list1 = [-2, 1, 3]
    list2 = [-5, 4, 6]

    result = merge_lists(list1, list2)

    assert result == [-5, -2, 1, 3, 4, 6]

def test_floats_return_correctly():
    list1 = [1, 2.2, 3]
    list2 = [4, 5.5, 6]

    result = merge_lists(list1, list2)

    assert result == [1, 2.2, 3, 4, 5.5, 6]

def test_lists_with_duplicates_correctly():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    result = merge_lists(list1, list2)

    assert result == [1, 2, 3]