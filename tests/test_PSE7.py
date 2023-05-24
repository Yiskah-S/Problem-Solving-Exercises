import pytest
from PSEs.PSE7_reshape_matrix import reshape_matrix


def test_convert_two_by_two_to_one_by_four():
    matrix = [[1,2],[3,4]]
    r = 1
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2,3,4]]

def test_cannot_reshape():
    matrix = [[1,2],[3,4]]
    r = 2
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2],[3,4]]

def test_convert_four_by_two_to_two_by_four():
    matrix = [[1,2],[3,4],[5,6],[7,8]]
    r = 2
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2,3,4],[5,6,7,8]]

def test_three_by_three_to_nine_by_one():
    # Arrange
    matrix = [[7, 2, 1], [4, 3, 5], [6, 9, 8]]
    r = 9
    c = 1

    # Act
    answer = reshape_matrix(matrix, r, c)

    # Assert
    assert answer == [[7], [2], [1], [4], [3], [5], [6], [9], [8]]

def test_empty_matrix():
    matrix = []
    r = 2
    c = 2

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == []

def test_single_row_matrix():
    matrix = [[1, 2, 3]]
    r = 1
    c = 3

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1, 2, 3]]

def test_single_column_matrix():
    matrix = [[1], [2], [3]]
    r = 3
    c = 1

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1], [2], [3]]

