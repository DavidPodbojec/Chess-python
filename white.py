def white_possible_moves(board, selected_piece):
    possible_moves = []
    
    def pawn_move():
        if board[selected_piece[0]-1][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]])
            
        if selected_piece[0] == 6 and board[selected_piece[0]-2][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]-2, selected_piece[1]])
            
        if board[selected_piece[0]-1][selected_piece[1]+1] % 10 != 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+1])
    
    def rook_move():
        print("white rook")
    
    def knight_move():
        print("white knight")
    
    def bishop_move():
        print("white bishop")
    
    def queen_move():
        print("white queen")
    
    def king_move():
        print("white king")
    
    
    piece = board[selected_piece[0]][selected_piece[1]]
    
    if piece == 10:
        king_move()
    elif piece == 20:
        queen_move()
    elif piece == 30:
        bishop_move()
    elif piece == 40:
        knight_move()
    elif piece == 50:
        rook_move()
    elif piece == 60:
        pawn_move()
    
    return possible_moves

def white_move(board, selected_piece, selected_square):
    piece = board[selected_piece[0]][selected_piece[1]]
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board