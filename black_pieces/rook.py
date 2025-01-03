def black_rook_move(board, selected_piece, possible_moves):
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
    
    return possible_moves
        