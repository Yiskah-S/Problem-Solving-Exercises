import pytest
from PSEs.PSE10_max_profit import max_profit

def test_max_profit_nominal():
    prices = [1, 2, 3, 4, 5]
    assert max_profit(prices) == 4

def test_max_profit_multiple_transactions():
    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit(prices) == 7

def test_max_profit_empty_array():
    prices = []
    assert max_profit(prices) == 0

def test_max_profit_single_element():
    prices = [7]
    assert max_profit(prices) == 0

def test_max_profit_decreasing_prices():
    prices = [7, 6, 4, 3, 1]
    assert max_profit(prices) == 0

def test_max_profit_increasing_prices():
    prices = [1, 2, 3, 4, 5, 6]
    assert max_profit(prices) == 5

def test_max_profit_duplicate_prices():
    prices = [7, 1, 5, 3, 3, 6]
    assert max_profit(prices) == 7

def test_max_profit_float_prices():
    prices = [1.2, 2.3, 3.4, 4.5, 5.6]
    assert max_profit(prices) == 4.4

def test_max_profit_large_values():
    prices = [1000000, 900000, 800000, 700000, 600000, 500000]
    assert max_profit(prices) == 0

def test_max_profit_large_values_profit():
    prices = [100000, 200000, 300000, 400000, 500000, 600000]
    assert max_profit(prices) == 500000
