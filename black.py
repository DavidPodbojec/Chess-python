def black_move(board, selected_piece):

    def pawn_move():
        if board[selected_piece[0]+1][selected_piece[1]] == 0:
            board[selected_piece[0]+1][selected_piece[1]] = str(board[selected_piece[0]+1][selected_piece[1]])  

        if board[selected_piece[0]+1][selected_piece[1]-1] != 0 and board[selected_piece[0]+1][selected_piece[1]] % 10 == 0:
            board[selected_piece[0]+1][selected_piece[1]-1] = str(board[selected_piece[0]+1][selected_piece[1]+1])



    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 11:
        pass
    elif piece == 22:
        pass
    elif piece == 33:
        pass
    elif piece == 44:
        pass
    elif piece == 55:
        pass
    elif piece == 66:
        pawn_move()
