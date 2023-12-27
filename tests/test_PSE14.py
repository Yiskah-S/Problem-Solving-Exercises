import pytest
from PSEs.PSE14_number_of_provinces import num_provinces

def test_example_1():
    # Arrange
    is_connected = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 2

def test_example_2():
    # Arrange
    is_connected = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 1

def test_example_3():
    # Arrange
    is_connected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 3

def test_returns_zero_for_empty_connections():
    # Arrange
    is_connected = []

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 0

def test_one_node_graph_returns_one():
    # Arrange
    is_connected = [[0]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 1

def test_graph_with_cycle():
    # Arrange
    is_connected = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 2

def test_large_graph_with_four_provinces():
    # Arrange
    is_connected = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 4

def test_example_1_with_self_loops():
    # Arrange
    is_connected = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 2

def test_example_2_with_self_loops():
    # Arrange
    is_connected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 1

def test_example_3_with_self_loops():
    # Arrange
    is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    # Act
    result = num_provinces(is_connected)

    # Assert
    assert result == 3
2

def test_invalid_graph():
    # Arrange
    is_connected_non_square = [
        [0, 1],
        [1, 0, 1]
    ]

    # Act
    result = num_provinces(is_connected_non_square)

    # Assert
    assert result == False

def test_invalid_node_value():
    # Arrange
    is_connected_invalid_node_value = [
        [0, ""],
        [1, 2]
    ]

    # Act
    result = num_provinces(is_connected_invalid_node_value)

    # Assert
    assert result == False