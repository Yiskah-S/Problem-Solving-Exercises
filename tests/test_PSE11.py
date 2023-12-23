import pytest
from PSEs.PSE11_most_frequent_k_elements import most_frequent_k_elements

def test_most_frequent_k_elements_nominal():
        # Arrange
        arr = [1,1,1,2,2,3]
        k = 2

        # Act
        result = most_frequent_k_elements(arr, k)

        # Assert
        assert set(result) == set([1,2])

def test_most_frequent_k_elements_single_arr():
    # Arrange
    arr = [1]
    k = 1 


    # Act
    result = most_frequent_k_elements(arr, k)

    # Act
    assert result == [1]

def test_most_frequent_k_elements_negative_number_case():
    # Arrange
    arr = [-1,-1,-1,-2,-5,-5,3,3,3,3,4]
    k = 3

    # Act
    result = most_frequent_k_elements(arr, k)

    # Assert
    assert set(result) == set([3,-1,-5])

def test_most_frequent_k_elements_empty_arr():
    # Arrange
    arr = []
    k = 0

    # Act
    result = most_frequent_k_elements(arr, k)

    # Assert
    assert result == []

def test_most_frequent_k_elements_k_greater_than_arr():
    # Arrange
    arr = [1,2,3,4,5]
    k = 10

    # Act
    result = most_frequent_k_elements(arr, k)

    # Assert
    assert set(result) == set([1,2,3,4,5])

def test_most_frequent_k_elements_k_is_zero():
    # Arrange
    arr = [1,2,3,4,5]
    k = 0

    # Act
    result = most_frequent_k_elements(arr, k)

    # Assert
    assert result == []

def test_most_frequent_k_elements_k_is_negative():
    # Arrange
    arr = [1,2,3,4,5]
    k = -1

    # Act
    result = most_frequent_k_elements(arr, k)

    # Assert
    assert result == []

