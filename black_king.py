from white import white_possible_moves

def is_check(board, black_king_position):
    #iterate through every opposite piece to see if their possible move is kings move
    check = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] % 10 == 0 and board[row][col] != 0:
                if black_king_position in white_possible_moves(board, (row, col)):
                    check = True

    return check
    
    

    
    