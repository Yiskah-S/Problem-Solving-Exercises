import pytest
from PSEs.ExamplePSE_rock_paper_scissors import winner

def test_rock_beats_scissors():
    # arrange
    player_1 = "rock"
    player_2 = "scissors"

    # act
    result = winner(player_1, player_2)

    # assert
    assert result == "Player 1 wins!"

def test_invalid_input():
    # arrange
    player_1 = "rock"
    player_2 = "lizards"

    # act
    result = winner(player_1, player_2)

    # assert
    assert result is None  