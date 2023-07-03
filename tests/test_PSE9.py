import pytest
from PSEs.PSE9_tic_tac_toe import tic_tac_toe_winner

def test_tie():
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]
    expected_result = 'Tie'
    assert tic_tac_toe_winner(board) == expected_result, f"Expected {expected_result}, but got {tic_tac_toe_winner(board)}"


def test_incomplete():
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', '', 'O']
    ]
    expected_result = None
    assert tic_tac_toe_winner(board) == expected_result, f"Expected {expected_result}, but got {tic_tac_toe_winner(board)}"


def test_col_win():
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'O', 'O']
    ]
    expected_result = 'O'
    assert tic_tac_toe_winner(board) == expected_result, f"Expected {expected_result}, but got {tic_tac_toe_winner(board)}"


def test_row_win():
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['X', 'X', 'O']
    ]
    expected_result = 'O'
    assert tic_tac_toe_winner(board) == expected_result, f"Expected {expected_result}, but got {tic_tac_toe_winner(board)}"


def test_diag_win():
    board = [
        ['O', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]
    expected_result = 'O'
    assert tic_tac_toe_winner(board) == expected_result, f"Expected {expected_result}, but got {tic_tac_toe_winner(board)}"
