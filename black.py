def black_move(board, selected_piece):
    print(selected_piece)
    def pawn_move():
        print("black pawn")
    
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
    elif piece == 22:
        queen_move()
    elif piece == 33:
        bishop_move()
    elif piece == 44:
        knight_move()
    elif piece == 55:
        rook_move()
    elif piece == 66:
        pawn_move()