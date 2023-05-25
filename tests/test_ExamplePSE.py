import pytest
from PSEs.ExamplePSE_rock_paper_scissors import winner

def test_rock_beats_scissors():
    player_1 = "rock"
    player_2 = "scissors"
    result = winner(player_1, player_2)
    assert result == "Player 1 wins!"

def test_invalid_input():
    player_1 = "rock"
    player_2 = "lizards"
    result = winner(player_1, player_2)
    assert result is None  

def test_paper_beats_rock():
    player_1 = "paper"
    player_2 = "rock"
    result = winner(player_1, player_2)
    assert result == "Player 1 wins!"

def test_scissors_beats_paper():
    player_1 = "scissors"
    player_2 = "paper"
    result = winner(player_1, player_2)
    assert result == "Player 1 wins!"

def test_rock_loses_to_paper():
    player_1 = "rock"
    player_2 = "paper"
    result = winner(player_1, player_2)
    assert result == "Player 2 wins!"

def test_scissors_loses_to_rock():
    player_1 = "scissors"
    player_2 = "rock"
    result = winner(player_1, player_2)
    assert result == "Player 2 wins!"

def test_paper_loses_to_scissors():
    player_1 = "paper"
    player_2 = "scissors"
    result = winner(player_1, player_2)
    assert result == "Player 2 wins!"

def test_rock_ties_with_rock():
    player_1 = "rock"
    player_2 = "rock"
    result = winner(player_1, player_2)
    assert result == "It's a tie!"
