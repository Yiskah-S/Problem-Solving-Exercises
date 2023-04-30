import pytest
from PSEs.PSE5_pairs_with_given_sum import pairs_with_given_sum

def test_valid_input():
    # Arrange
    numbers = [1, 2, 4, 5]
    target = 6
    
    # Act
    result = pairs_with_given_sum(numbers, target)
    
    # Assert
    assert result == 2

def test_empty_input():
    # Arrange
    numbers = []
    target = 6
    
    # Act/Assert
    with pytest.raises(ValueError):
        pairs_with_given_sum(numbers, target)

def test_negative_numbers():
    # Arrange
    numbers1 = [-1, 2, -3, 4, 5]
    target1 = 1
    
    numbers2 = [-1, -2, -3, -4, -5]
    target2 = -7
    
    # Act
    result1 = pairs_with_given_sum(numbers1, target1)
    result2 = pairs_with_given_sum(numbers2, target2)
    
    # Assert
    assert result1 == 2
    assert result2 == 2

def test_no_pairs():
    # Arrange
    numbers = [1, 2, 3, 4, 5]
    target = 10
    
    # Act
    result = pairs_with_given_sum(numbers, target)
    
    # Assert
    assert result == 0

def test_floats():
    # Arrange
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    target = 7.7
    
    # Act
    result = pairs_with_given_sum(numbers, target)
    
    # Assert
    assert result == 2

def test_duplicate_numbers():
    # Arrange
    numbers = [1, 2, 2, 3, 4, 4, 5, 5]
    target = 6

    # Act
    result = pairs_with_given_sum(numbers, target)

    # Assert
    assert result == 3

def test_list_with_not_numbers():
    # Arrange
    numbers = ["apple", "banana", "cherry", 1, 4, True, False, None, [1, 2], {"key": "value"}]
    target = 5

    # Act
    result = pairs_with_given_sum(numbers, target)

    # Assert
    assert result == 1

def test_no_numbers_in_list():
    # Arrange
    numbers = ["apple", "banana", "cherry"]
    target = 5

    # Act/Assert
    try:
        pairs_with_given_sum(numbers, target)
    except ValueError as err:
        assert str(err) == "List contains no numbers"
    else:
        assert False, "Expected ValueError"

def test_insufficient_numbers_in_list():
    # Arrange
    numbers = [1]
    target = 6

    # Act/Assert
    try:
        pairs_with_given_sum(numbers, target)
    except ValueError as e:
        assert str(e) == "List contains insufficient numbers to make pairs"
    else:
        assert False, "Expected ValueError"

def test_invalid_target_type():
    # Arrange
    numbers = [1, 2, 3, 4, 5]
    target = "invalid"

    # Act/Assert
    try:
        pairs_with_given_sum(numbers, target)
    except TypeError as e:
        assert str(e) == "Invalid target input"
    else:
        assert False, "Expected TypeError"

def test_empty_input_list():
    # Arrange
    numbers = []
    target = 6

    # Act/Assert
    try:
        pairs_with_given_sum(numbers, target)
    except ValueError as e:
        assert str(e) == "Invalid input list"
    else:
        assert False, "Expected ValueError"

