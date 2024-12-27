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
        count = 8 - selected_piece[0]
        
        for i in range(1, count):
            
            if board[selected_piece[0]+i][selected_piece[1]] % 10 == 0 and board[selected_piece[0]+i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
                
                break
            elif board[selected_piece[0]+i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
            
            else:
                break
            
        
        #up        
        for i in range(1, selected_piece[0]+1):
            if board[selected_piece[0]-i][selected_piece[1]] % 10 == 0 and board[selected_piece[0]-i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
                
                break
            elif board[selected_piece[0]-i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
            
            else:
                break
            
        #left 
        for i in range(1, selected_piece[1]+1):
            if board[selected_piece[0]][selected_piece[1]-i] % 10 == 0 and board[selected_piece[0]][selected_piece[1]-i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
                break
            elif board[selected_piece[0]][selected_piece[1]-i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
            else:
                break
            
        #right
        for i in range(1, 8-selected_piece[1]):
            
            if board[selected_piece[0]][selected_piece[1]+i] % 10 == 0 and board[selected_piece[0]][selected_piece[1]+i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-+i])
                break
            elif board[selected_piece[0]][selected_piece[1]+i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]+i])
            else:
                break
            
            
    
    def bishop_move():
        #down left
        if selected_piece[0] != 7 and selected_piece[1] != 0:
            count = 2
            if min(8-selected_piece[0], selected_piece[1]+1) > 1:
                count = min(8-selected_piece[0], selected_piece[1]+1)
                
            
            for i in range(1, count):
                if board[selected_piece[0]+i][selected_piece[1]-i] == 0: 
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
                elif board[selected_piece[0]+i][selected_piece[1]-i] % 10 == 0:
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
                    break                   
                
                else:
                    break
            
        #down right  
        if selected_piece[0] != 7 and selected_piece[1] != 7:
            count = 2
            
            if min(8-selected_piece[0], 8-selected_piece[1]) > 1:
                count = min(8-selected_piece[0], 8- selected_piece[1])
            
            for i in range(1, count):
                if board[selected_piece[0]+i][selected_piece[1]+i] == 0: 
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]+i])
                elif board[selected_piece[0]+i][selected_piece[1]+i] % 10 == 0:
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]+i])
                    break
                    
                else:
                    break
                    
        #up left
        if selected_piece[0] != 0 and selected_piece[1] != 0:
            count = 2
            if min(selected_piece[0]+1, selected_piece[1]+1) > 1:
                count = min(selected_piece[0]+1, selected_piece[1]+1)
            
            for i in range(1, count):
                
                if board[selected_piece[0]-i][selected_piece[1]-i] == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]-i])
                elif board[selected_piece[0]-i][selected_piece[1]-i] % 10 == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]-i])
                    break
                    
                else:
                    break
                    
        #up right 
        if selected_piece[0] != 0 and selected_piece[1] != 7:
            count = 2
            if min(selected_piece[0]+1, 8-selected_piece[1]) > 1:
                count = min(selected_piece[0]+1, 8-selected_piece[1])
            
            
            for i in range(1, count):
                if board[selected_piece[0]-i][selected_piece[1]+i] == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                elif board[selected_piece[0]-i][selected_piece[1]+i] % 10 == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                    break

                else:
                    break
    
    def queen_move():
        #down
        count = 8 - selected_piece[0]
        
        for i in range(1, count):
            
            if board[selected_piece[0]+i][selected_piece[1]] % 10 == 0 and board[selected_piece[0]+i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
                
                break
            elif board[selected_piece[0]+i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
            
            else:
                break
            
        
        #up        
        for i in range(1, selected_piece[0]+1):
            if board[selected_piece[0]-i][selected_piece[1]] % 10 == 0 and board[selected_piece[0]-i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
                
                break
            elif board[selected_piece[0]-i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
            
            else:
                break
            
        #left 
        for i in range(1, selected_piece[1]+1):
            if board[selected_piece[0]][selected_piece[1]-i] % 10 == 0 and board[selected_piece[0]][selected_piece[1]-i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
                break
            elif board[selected_piece[0]][selected_piece[1]-i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
            else:
                break
            
        #right
        for i in range(1, 8-selected_piece[1]):
            
            if board[selected_piece[0]][selected_piece[1]+i] % 10 == 0 and board[selected_piece[0]][selected_piece[1]+i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-+i])
                break
            elif board[selected_piece[0]][selected_piece[1]+i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]+i])
            else:
                break
            
        #down left
        if selected_piece[0] != 7 and selected_piece[1] != 0:
            count = 2
            if min(8-selected_piece[0], selected_piece[1]+1) > 1:
                count = min(8-selected_piece[0], selected_piece[1]+1)
                
            
            for i in range(1, count):
                if board[selected_piece[0]+i][selected_piece[1]-i] == 0: 
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
                elif board[selected_piece[0]+i][selected_piece[1]-i] % 10 == 0:
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
                    break                   
                
                else:
                    break
            
        #down right  
        if selected_piece[0] != 7 and selected_piece[1] != 7:
            count = 2
            
            if min(8-selected_piece[0], 8-selected_piece[1]) > 1:
                count = min(8-selected_piece[0], 8- selected_piece[1])
            
            for i in range(1, count):
                if board[selected_piece[0]+i][selected_piece[1]+i] == 0: 
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]+i])
                elif board[selected_piece[0]+i][selected_piece[1]+i] % 10 == 0:
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]+i])
                    break
                    
                else:
                    break
                    
        #up left
        if selected_piece[0] != 0 and selected_piece[1] != 0:
            count = 2
            if min(selected_piece[0]+1, selected_piece[1]+1) > 1:
                count = min(selected_piece[0]+1, selected_piece[1]+1)
            
            for i in range(1, count):
                
                if board[selected_piece[0]-i][selected_piece[1]-i] == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]-i])
                elif board[selected_piece[0]-i][selected_piece[1]-i] % 10 == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]-i])
                    break
                    
                else:
                    break
                    
        #up right 
        if selected_piece[0] != 0 and selected_piece[1] != 7:
            count = 2
            if min(selected_piece[0]+1, 8-selected_piece[1]) > 1:
                count = min(selected_piece[0]+1, 8-selected_piece[1])
            
            
            for i in range(1, count):
                if board[selected_piece[0]-i][selected_piece[1]+i] == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                elif board[selected_piece[0]-i][selected_piece[1]+i] % 10 == 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                    break

                else:
                    break
        
    
    def king_move():
        #down
        if selected_piece[0] != 7 and board[selected_piece[0]+1][selected_piece[1]] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]]) 
        
        #up
        if selected_piece[0] != 0 and board[selected_piece[0]-1][selected_piece[1]] % 10 == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]])
        
        #left
        if selected_piece[1] != 0 and board[selected_piece[0]][selected_piece[1]-1] % 10 == 0:
            possible_moves.append([selected_piece[0], selected_piece[1]-1])
        
        #right            
        if selected_piece[1] != 7 and board[selected_piece[0]][selected_piece[1]+1] % 10 == 0:
            possible_moves.append([selected_piece[0], selected_piece[1]+1])
            
        #down left
        if selected_piece[0] != 7 and selected_piece[1] != 0 and board[selected_piece[0]+1][selected_piece[1]-1] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]-1])
            
        #down right
        if selected_piece[0] != 7 and selected_piece[1] != 7 and board[selected_piece[0]+1][selected_piece[1]+1] % 10 == 0:
            possible_moves.append([selected_piece[0]+1, selected_piece[1]+1])
            
        #up left
        if selected_piece[0] != 0 and selected_piece[1] != 0 and board[selected_piece[0]-1][selected_piece[1]-1] % 10 == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]-1])
            
        #up right
        if selected_piece[0] != 0 and selected_piece[1] != 7 and board[selected_piece[0]-1][selected_piece[1]+1] % 10 == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+1])
    

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