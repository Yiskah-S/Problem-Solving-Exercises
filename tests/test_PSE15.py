import pytest
from PSEs.PSE15_network_delay import network_delay_time

def test_network_delay_returns_correct_result_for_small_connected_graph():
    # Arrange
    times = [
        [2,1,1],
        [2,3,1],
        [3,4,1]
    ]
    n = 4
    source = 2

    # Act
    answer = network_delay_time(times, n, source)

    # Assert
    assert answer == 2

def test_network_delay_returns_minus_1_when_node_unreachable():
    # Arrange
    times = [
        [2,1,1],
        [2,3,2],
        [3,1,1]
    ]
    n = 3
    source = 1

    # Act
    answer = network_delay_time(times, n, source)

    # Assert
    assert answer == -1

def test_network_delay_returns_minus_1_for_disconnected_graph():
    # Arrange
    times = [
        [2,3,2]
    ]
    n = 3
    source = 2

    # Act
    answer = network_delay_time(times, n, source)

    # Assert
    assert answer == -1

def test_network_delay_returns_correct_result_for_larger_graph():
    # Arrange
    times = [
        [1, 2, 3],
        [2, 4, 1],
        [2, 5, 5],
        [2, 3, 6],
        [3, 5, 6],
        [4, 5, 7]
    ]
    n = 5
    source = 1

    # Act
    answer = network_delay_time(times, n, source)

    # Assert
    assert answer == 9



def test_with_negative_weights():
    with pytest.raises(ValueError):
        network_delay_time([[1, 2, -3]], 2, 1)

def test_empty_times_list():
    with pytest.raises(ValueError):
        network_delay_time([], 3, 1)

def test_invalid_node_numbers():
    with pytest.raises(ValueError):
        network_delay_time([[0, 2, 1]], 2, 1)

def test_invalid_source_node():
    with pytest.raises(ValueError):
        network_delay_time([[1, 2, 1]], 2, 3)

def test_non_integer_input():
    with pytest.raises(ValueError):
        network_delay_time([["a", 2, 1]], 2, 1)