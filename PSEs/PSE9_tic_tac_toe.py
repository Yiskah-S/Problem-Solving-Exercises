def tic_tac_toe_winner(board):
    for row in board:
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        if board[0][col] != ' ' and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != '') or (board[0][2] == board[1][1] == board[2][0] and board[0][2] != ''):
        return board[2][2]

    if not any(cell == '' for row in board for cell in row):
        return 'Tie'

    return None
