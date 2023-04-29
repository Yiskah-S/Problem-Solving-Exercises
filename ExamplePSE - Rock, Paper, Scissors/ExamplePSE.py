def winner(player_1, player_2):
    VALID_CHOICES = ('rock', 'paper', 'scissors')
    
    if not (player_1 in VALID_CHOICES and player_2 in VALID_CHOICES):
        return None
    elif player_1 == player_2:
        return "It's a tie!"
    elif player_1 == 'paper' and player_2 == 'rock':
            return "Player 1 wins!"
    elif player_1 == 'rock' and player_2 == 'scissors':
            return "Player 1 wins!"
    elif player_1 == 'scissors' and player_2 == 'paper':
            return "Player 1 wins!"
    else:
        return "Player 2 wins!"