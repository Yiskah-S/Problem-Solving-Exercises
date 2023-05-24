import pytest
from PSEs.PSE8_kth_missing_positive_num import kth_missing_positive_number

def test_nominal_case():
    arr = [2, 3, 4, 7, 11]
    k = 5
    expected_output = 9
    assert kth_missing_positive_number(arr, k) == expected_output

def test_edge_case():
    arr = [1, 2, 3, 4]
    k = 2
    expected_output = 6
    assert kth_missing_positive_number(arr, k) == expected_output

def test_empty_array():
    arr = []
    k = 5
    with pytest.raises(Exception):
        kth_missing_positive_number(arr, k)

def test_negative_k():
    arr = [1, 2, 3, 4]
    k = -1
    with pytest.raises(Exception):
        kth_missing_positive_number(arr, k)

def test_large_array():
    arr = [1, 1010]
    k = 1000
    expected_output = 1001
    assert kth_missing_positive_number(arr, k) == expected_output

def test_large_numbers():
    arr = [10**9, 10**9 + 3]
    k = 3
    expected_output = 3
    assert kth_missing_positive_number(arr, k) == expected_output

