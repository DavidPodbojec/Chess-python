def black_possible_moves(board, selected_piece):
    possible_moves = []
    
    def pawn_move():
        if board[selected_piece[0]+1][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]])
            
        if selected_piece[0] == 1 and board[selected_piece[0]+2][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]+2, selected_piece[1]])
    
    def knight_move():
        print("black knight")
    
    def rook_move():
        print("black rook")
    
    def bishop_move():
        print("black bishop")
    
    def queen_move():
        print("black queen")
    
    def king_move():
        print("black king")
    

    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 11:
        king_move()
    elif piece == 21:
        queen_move()
    elif piece == 31:
        bishop_move()
    elif piece == 41:
        knight_move()
    elif piece == 51:
        rook_move()
    elif piece == 61:
        pawn_move()
        
    return possible_moves

def black_move(board, selected_piece, selected_square):
    piece = board[selected_piece[0]][selected_piece[1]]
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board