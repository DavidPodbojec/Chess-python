def black_possible_moves(board, selected_piece):
    possible_moves = []
    
    def pawn_move():
        #pawn one move up
        if board[selected_piece[0]+1][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]])
            
        #two moves up
        if selected_piece[0] == 1 and board[selected_piece[0]+2][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]+2, selected_piece[1]])
        
        #take right
        if selected_piece[1] != 7 and board[selected_piece[0]+1][selected_piece[1]+1] != 0 and board[selected_piece[0]+1][selected_piece[1]+1] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]+1])
            
        #take left
        if  selected_piece[1] != 0 and board[selected_piece[0]+1][selected_piece[1]-1] != 0 and board[selected_piece[0]+1][selected_piece[1]-1] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]-1]) 
    
    def knight_move():
        #down left
        if selected_piece[0] <= 5 and selected_piece[1] >= 1 and board[selected_piece[0]+2][selected_piece[1]-1] % 10 == 0:
            possible_moves.append([selected_piece[0]+2, selected_piece[1]-1]) 
            
        #down right
        if selected_piece[0] <= 5 and selected_piece[1] <= 6 and board[selected_piece[0]+2][selected_piece[1]+1] % 10 == 0:
            possible_moves.append([selected_piece[0]+2, selected_piece[1]+1]) 
            
        #left up
        if selected_piece[0] >= 1 and selected_piece[1] >= 2 and board[selected_piece[0]-1][selected_piece[1]-2] % 10 == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]-2])
            
        #left down
        if selected_piece[0] <= 6 and selected_piece[1] >= 2 and board[selected_piece[0]+1][selected_piece[1]-2] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]-2])
            
        #right up
        if selected_piece[0] >= 1 and selected_piece[1] <= 5 and board[selected_piece[0]-1][selected_piece[1]+2] % 10 == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+2])
            
        #right down
        if selected_piece[0] <= 6 and selected_piece[1] <= 5 and board[selected_piece[0]+1][selected_piece[1]+2] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]+2])
            
        #up left
        if selected_piece[0] >= 2 and selected_piece[1] >= 1 and board[selected_piece[0]-2][selected_piece[1]-1] % 10 == 0:
            possible_moves.append([selected_piece[0]-2, selected_piece[1]-1])
            
        #up right 
        if selected_piece[0] >= 2 and selected_piece[1] <= 6 and board[selected_piece[0]-2][selected_piece[1]+1] % 10 == 0:
            possible_moves.append([selected_piece[0]-2, selected_piece[1]+1])
        
    
    def rook_move():
        #down
        print(selected_piece[0])
        count = 8 - selected_piece[0]
        
        for i in range(count):
            if board[selected_piece[0]+i][selected_piece[1]] % 10 == 0:
                break
            elif board[selected_piece[0]+i][selected_piece[1]] % 10 == 0 and board[selected_piece[0]+i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
            
            elif board[selected_piece[0]+i][selected_piece[1]] % 10 == 0 and board[selected_piece[0]+i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
                break
            
            
            
    
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
    #switch the square of piece with the selected square
    piece = board[selected_piece[0]][selected_piece[1]]
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board