import pytest
from PSEs.PSE5_pairs_with_given_sum import pairs_with_given_sum

def test_valid_input():
    numbers = [1, 2, 4, 5]
    target = 6
    
    result = pairs_with_given_sum(numbers, target)

    assert result == 2

def test_empty_input():
    numbers = []
    target = 6

    with pytest.raises(ValueError):
        pairs_with_given_sum(numbers, target)

def test_negative_numbers():
    numbers1 = [-1, 2, -3, 4, 5]
    target1 = 1
    numbers2 = [-1, -2, -3, -4, -5]
    target2 = -7
    
    result1 = pairs_with_given_sum(numbers1, target1)
    result2 = pairs_with_given_sum(numbers2, target2)
    
    assert result1 == 2
    assert result2 == 2

def test_no_pairs():
    numbers = [1, 2, 3, 4, 5]
    target = 10
    
    result = pairs_with_given_sum(numbers, target)
    
    assert result == 0

def test_floats():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    target = 7.7
    
    result = pairs_with_given_sum(numbers, target)
    

    assert result == 2

def test_duplicate_numbers():
    numbers = [1, 2, 2, 3, 4, 4, 5, 5]
    target = 6

    result = pairs_with_given_sum(numbers, target)

    assert result == 3

def test_list_with_not_numbers():
    numbers = ["apple", "banana", "cherry", 1, 4, True, False, None, [1, 2], {"key": "value"}]
    target = 5

    result = pairs_with_given_sum(numbers, target)

    assert result == 1

def test_no_numbers_in_list():
    numbers = ["apple", "banana", "cherry"]
    target = 5

    try:
        pairs_with_given_sum(numbers, target)
    except ValueError as err:
        assert str(err) == "List contains no numbers"
    else:
        assert False, "Expected ValueError"

def test_insufficient_numbers_in_list():
    numbers = [1]
    target = 6

    try:
        pairs_with_given_sum(numbers, target)
    except ValueError as e:
        assert str(e) == "List contains insufficient numbers to make pairs"
    else:
        assert False, "Expected ValueError"

def test_invalid_target_type():
    numbers = [1, 2, 3, 4, 5]
    target = "invalid"

    try:
        pairs_with_given_sum(numbers, target)
    except TypeError as e:
        assert str(e) == "Invalid target input"
    else:
        assert False, "Expected TypeError"

def test_empty_input_list():
    numbers = []
    target = 6

    try:
        pairs_with_given_sum(numbers, target)
    except ValueError as e:
        assert str(e) == "Invalid input list"
    else:
        assert False, "Expected ValueError"

