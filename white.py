rook1_moved = 0
rook2_moved = 0
king_moved = 0

def white_possible_moves(board, selected_piece):
    global rook1_moved
    global rook2_moved
    global king_moved
    
    possible_moves = []
    
    def white_pawn_move():
        #move one up
        if board[selected_piece[0]-1][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]])
            
        #move two up
        if selected_piece[0] == 6 and board[selected_piece[0]-2][selected_piece[1]] == 0:
            possible_moves.append([selected_piece[0]-2, selected_piece[1]])
            
        #take right
        if selected_piece[1] != 7 and board[selected_piece[0]-1][selected_piece[1]+1] % 10 != 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+1])
            
        #take left
        if selected_piece[1] != 0 and board[selected_piece[0]-1][selected_piece[1]-1] % 10 != 0:
            possible_moves.append([selected_piece[0]-1, selected_piece[1]-1])
            
    
    def white_rook_move():
        #down
        count = 8 - selected_piece[0]
        
        for i in range(1, count):
            
            if board[selected_piece[0]+i][selected_piece[1]] % 10 != 0 and board[selected_piece[0]+i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])                
                break
            
            elif board[selected_piece[0]+i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
            
            else:
                break
            
        
        #up        
        for i in range(1, selected_piece[0]+1):
            if board[selected_piece[0]-i][selected_piece[1]] % 10 != 0 and board[selected_piece[0]-i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
                
                break
            elif board[selected_piece[0]-i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
            
            else:
                break
            
        #left 
        for i in range(1, selected_piece[1]+1):
            if board[selected_piece[0]][selected_piece[1]-i] % 10 != 0 and board[selected_piece[0]][selected_piece[1]-i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
                break
            elif board[selected_piece[0]][selected_piece[1]-i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
            else:
                break
            
        #right
        for i in range(1, 8-selected_piece[1]):
            
            if board[selected_piece[0]][selected_piece[1]+i] % 10 != 0 and board[selected_piece[0]][selected_piece[1]+i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-+i])
                break
            elif board[selected_piece[0]][selected_piece[1]+i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]+i])
            else:
                break
            
    
    def white_knight_move():
        #down left
        if selected_piece[0] <= 5 and selected_piece[1] >= 1 and (board[selected_piece[0]+2][selected_piece[1]-1] % 10 != 0 or board[selected_piece[0]+2][selected_piece[1]-1] == 0):
            possible_moves.append([selected_piece[0]+2, selected_piece[1]-1]) 
            
        #down right
        if selected_piece[0] <= 5 and selected_piece[1] <= 6 and (board[selected_piece[0]+2][selected_piece[1]+1] % 10 != 0 or board[selected_piece[0]+2][selected_piece[1]+1] == 0):
            possible_moves.append([selected_piece[0]+2, selected_piece[1]+1]) 
            
        #left up
        if selected_piece[0] >= 1 and selected_piece[1] >= 2 and (board[selected_piece[0]-1][selected_piece[1]-2] % 10 != 0 or board[selected_piece[0]-1][selected_piece[1]-2] == 0):
            possible_moves.append([selected_piece[0]-1, selected_piece[1]-2])
            
        #left down
        if selected_piece[0] <= 6 and selected_piece[1] >= 2 and (board[selected_piece[0]+1][selected_piece[1]-2] % 10 != 0 or board[selected_piece[0]+1][selected_piece[1]-2] == 0):
            possible_moves.append([selected_piece[0]+1, selected_piece[1]-2])
            
        #right up
        if selected_piece[0] >= 1 and selected_piece[1] <= 5 and (board[selected_piece[0]-1][selected_piece[1]+2] % 10 != 0 or board[selected_piece[0]-1][selected_piece[1]+2] == 0):
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+2])
            
        #right down
        if selected_piece[0] <= 6 and selected_piece[1] <= 5 and (board[selected_piece[0]+1][selected_piece[1]+2] % 10 != 0 or board[selected_piece[0]+1][selected_piece[1]+2] == 0):
            possible_moves.append([selected_piece[0]+1, selected_piece[1]+2])
            
        #up left
        if selected_piece[0] >= 2 and selected_piece[1] >= 1 and (board[selected_piece[0]-2][selected_piece[1]-1] % 10 != 0 or board[selected_piece[0]-2][selected_piece[1]-1] == 0):
            possible_moves.append([selected_piece[0]-2, selected_piece[1]-1])
            
        #up right 
        if selected_piece[0] >= 2 and selected_piece[1] <= 6 and (board[selected_piece[0]-2][selected_piece[1]+1] % 10 != 0 or board[selected_piece[0]-2][selected_piece[1]+1] == 0):
            possible_moves.append([selected_piece[0]-2, selected_piece[1]+1])
    
    def white_bishop_move():
        #down left
        if selected_piece[0] != 7 and selected_piece[1] != 0:
            count = 2
            if min(8-selected_piece[0], selected_piece[1]+1) > 1:
                count = min(8-selected_piece[0], selected_piece[1]+1)
                
            
            for i in range(1, count):
                if board[selected_piece[0]+i][selected_piece[1]-i] == 0: 
                    possible_moves.append([selected_piece[0]+i, selected_piece[1]-i])
                elif board[selected_piece[0]+i][selected_piece[1]-i] % 10 != 0:
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
                elif board[selected_piece[0]+i][selected_piece[1]+i] % 10 != 0:
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
                elif board[selected_piece[0]-i][selected_piece[1]-i] % 10 != 0:
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
                elif board[selected_piece[0]-i][selected_piece[1]+i] % 10 != 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                    break

                else:
                    break
            
    
    def white_queen_move():
        #down
        count = 8 - selected_piece[0]
        
        for i in range(1, count):
            
            if board[selected_piece[0]+i][selected_piece[1]] % 10 != 0 and board[selected_piece[0]+i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])                
                break
            
            elif board[selected_piece[0]+i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]+i, selected_piece[1]])
            
            else:
                break
            
        
        #up        
        for i in range(1, selected_piece[0]+1):
            if board[selected_piece[0]-i][selected_piece[1]] % 10 != 0 and board[selected_piece[0]-i][selected_piece[1]] != 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
                
                break
            elif board[selected_piece[0]-i][selected_piece[1]] == 0:
                possible_moves.append([selected_piece[0]-i, selected_piece[1]])
            
            else:
                break
            
        #left 
        for i in range(1, selected_piece[1]+1):
            if board[selected_piece[0]][selected_piece[1]-i] % 10 != 0 and board[selected_piece[0]][selected_piece[1]-i] != 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
                break
            elif board[selected_piece[0]][selected_piece[1]-i] == 0:
                possible_moves.append([selected_piece[0], selected_piece[1]-i])
            else:
                break
            
        #right
        for i in range(1, 8-selected_piece[1]):
            
            if board[selected_piece[0]][selected_piece[1]+i] % 10 != 0 and board[selected_piece[0]][selected_piece[1]+i] != 0:
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
                elif board[selected_piece[0]+i][selected_piece[1]-i] % 10 != 0:
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
                elif board[selected_piece[0]+i][selected_piece[1]+i] % 10 != 0:
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
                elif board[selected_piece[0]-i][selected_piece[1]-i] % 10 != 0:
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
                elif board[selected_piece[0]-i][selected_piece[1]+i] % 10 != 0:
                    possible_moves.append([selected_piece[0]-i, selected_piece[1]+i])
                    break

                else:
                    break
    
    def white_king_move():
        #down
        if selected_piece[0] != 7 and (board[selected_piece[0]+1][selected_piece[1]] % 10 != 0 or board[selected_piece[0]+1][selected_piece[1]] == 0):
            possible_moves.append([selected_piece[0]+1, selected_piece[1]]) 
        
        #up
        if selected_piece[0] != 0 and (board[selected_piece[0]-1][selected_piece[1]] % 10 != 0 or board[selected_piece[0]-1][selected_piece[1]] == 0):
            possible_moves.append([selected_piece[0]-1, selected_piece[1]])
        
        #left
        if selected_piece[1] != 0 and (board[selected_piece[0]][selected_piece[1]-1] % 10 != 0 or board[selected_piece[0]][selected_piece[1]-1] == 0):
            possible_moves.append([selected_piece[0], selected_piece[1]-1])
        
        #right            
        if selected_piece[1] != 7 and (board[selected_piece[0]][selected_piece[1]+1] % 10 != 0 or board[selected_piece[0]][selected_piece[1]+1] == 0):
            possible_moves.append([selected_piece[0], selected_piece[1]+1])
            
        #down left
        if selected_piece[0] != 7 and selected_piece[1] != 0 and (board[selected_piece[0]+1][selected_piece[1]-1] % 10 != 0 or board[selected_piece[0]+1][selected_piece[1]-1] == 0):
            possible_moves.append([selected_piece[0]+1, selected_piece[1]-1])
            
        #down right
        if selected_piece[0] != 7 and selected_piece[1] != 7 and (board[selected_piece[0]+1][selected_piece[1]+1] % 10 != 0 or board[selected_piece[0]+1][selected_piece[1]+1] == 0):
            possible_moves.append([selected_piece[0]+1, selected_piece[1]+1])
            
        #up left
        if selected_piece[0] != 0 and selected_piece[1] != 0 and (board[selected_piece[0]-1][selected_piece[1]-1] % 10 != 0 or board[selected_piece[0]-1][selected_piece[1]-1] == 0):
            possible_moves.append([selected_piece[0]-1, selected_piece[1]-1])
            
        #up right
        if selected_piece[0] != 0 and selected_piece[1] != 7 and (board[selected_piece[0]-1][selected_piece[1]+1] % 10 != 0 or board[selected_piece[0]-1][selected_piece[1]+1] == 0):
            possible_moves.append([selected_piece[0]-1, selected_piece[1]+1])
            
        #castle left
        if king_moved == 0 and rook1_moved == 0:
            castle = True
            for i in range(1, 4):
                
                if board[selected_piece[0]][selected_piece[1]-i] != 0:
                    castle = False 
                    
            if castle:
                possible_moves.append([selected_piece[0], selected_piece[1]-2])
                
        #castle right
        if king_moved == 0 and rook2_moved == 0:
            castle = True
            for i in range(1, 3):
                print(i)
                if board[selected_piece[0]][selected_piece[1]+i] != 0:
                    castle = False 
                    
            if castle:
                possible_moves.append([selected_piece[0], selected_piece[1]+2])
               
    piece = board[selected_piece[0]][selected_piece[1]]
    
    if piece == 10:
        white_king_move()
    elif piece == 20:
        white_queen_move()
    elif piece == 30:
        white_bishop_move()
    elif piece == 40:
        white_knight_move()
    elif piece == 50:
        white_rook_move()
    elif piece == 60:
        white_pawn_move()
    
    return possible_moves

def white_move(board, selected_piece, selected_square):
    piece = board[selected_piece[0]][selected_piece[1]]
        
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board

def white_real_move(board, selected_piece, selected_square):
    global rook2_moved
    global rook1_moved
    global king_moved
    
    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 10:
        
        #improve caste so that it can't be done when a piece is checked
        if king_moved == 0 and selected_square == (7, 2) and rook1_moved == 0:
            king_moved = 1
            rook1_moved = 1
            board[7][0] = 0
            board[7][3] = 50

          
        if king_moved == 0 and selected_square == (7, 6) and rook2_moved == 0:
            
            king_moved = 1
            rook2_moved = 1
            board[7][7] = 0
            board[7][5] = 50
    
    if piece == 50 and selected_piece == (7, 0):
        rook1_moved = 1
    
    if piece == 50 and selected_piece == (7, 7):
        rook2_moved = 1
        
    
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board