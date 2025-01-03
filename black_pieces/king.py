import initial_state

def black_king_move(board, selected_piece, possible_moves):
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
            
        #castle left
        if initial_state.black_king_moved == 0 and initial_state.black_rook1_moved == 0:
            castle = True
            for i in range(1, 4):
                if board[selected_piece[0]][selected_piece[1]-i] != 0:
                    castle = False 

            if castle:
                possible_moves.append([selected_piece[0], selected_piece[1]-2])
                
        #castle right
        if initial_state.black_king_moved == 0 and initial_state.black_rook2_moved == 0:
            castle = True
            for i in range(1, 3):
                if board[selected_piece[0]][selected_piece[1]+i] != 0:
                    castle = False

            if castle:
                possible_moves.append([selected_piece[0], selected_piece[1]+2])