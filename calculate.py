from white import white_possible_moves
from black import black_possible_moves
import copy
import initial_state

def black_is_checkmate(board, king_position):
    moves = []
    selected_piece = ()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] % 10 != 0:
                selected_piece = (row, col)
                piece = board[row][col]

                possible_moves = black_possible_moves(board, selected_piece)

                if black_is_check(board, king_position):
                    new_possible_moves = []
                    for move in possible_moves:
                        temp_board = copy.deepcopy(board)
                        temp_board = black_move(temp_board, selected_piece, (move[0], move[1]))

                        if piece == 11:
                            for king_move in possible_moves:
                                if black_is_check(temp_board, king_move) == False:
                                    new_possible_moves.append(king_move)
                        
                        elif black_is_check(temp_board, king_position) == False:
                            new_possible_moves.append(move)


                    possible_moves = new_possible_moves

                moves_to_remove = []        
                for piece_move in possible_moves:
                    temp_board = copy.deepcopy(board)
                    temp_board = black_move(temp_board, selected_piece, (piece_move[0], piece_move[1]))
                    
                    if black_is_check(temp_board, king_position) == True and piece != 11:
                        moves_to_remove.append(piece_move)
                    elif piece == 11:
                        if black_is_check(temp_board, piece_move) == True:
                            moves_to_remove.append(piece_move)

                for move in moves_to_remove:
                    possible_moves.remove(move)
                    
                if possible_moves != []:
                    for move in possible_moves:
                        moves.append(move)
    
    if moves == []:
        return True
    else:
        return False
    

def white_is_checkmate(board, king_position):
    moves = []
    selected_piece = ()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] % 10 == 0 and board[row][col] != 0:
                selected_piece = (row, col)
                piece = board[row][col]

                possible_moves = white_possible_moves(board, selected_piece)

                if white_is_check(board, king_position):
                    new_possible_moves = []
                    for move in possible_moves:
                        temp_board = copy.deepcopy(board)
                        temp_board = white_move(temp_board, selected_piece, (move[0], move[1]))

                        if piece == 10:
                            for king_move in possible_moves:
                                if white_is_check(temp_board, king_move) == False:
                                    new_possible_moves.append(king_move)
                        
                        elif white_is_check(temp_board, king_position) == False:
                            new_possible_moves.append(move)
                            

                    possible_moves = new_possible_moves

                moves_to_remove = []        
                for piece_move in possible_moves:
                    temp_board = copy.deepcopy(board)
                    temp_board = white_move(temp_board, selected_piece, (piece_move[0], piece_move[1]))
                    
                    if white_is_check(temp_board, king_position) == True and piece != 10:
                        moves_to_remove.append(piece_move)
                    elif piece == 10:
                        if white_is_check(temp_board, piece_move) == True:
                            moves_to_remove.append(piece_move)

                for move in moves_to_remove:
                    possible_moves.remove(move)
                    
                if possible_moves != []:
                    for move in possible_moves:
                        moves.append(move)
    
    if moves == []:
        return True
    else:
        return False
                

def black_is_check(board, black_king_position):
    
    check = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] % 10 == 0 and board[row][col] != 0:
                if black_king_position in white_possible_moves(board, (row, col)):
                    check = True

    return check

def white_is_check(board, white_king_position):
    
    check = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] % 10 != 0 and board[row][col] != 0:
                if white_king_position in black_possible_moves(board, (row, col)):
                    check = True

    return check

def calculate(board, selected_piece):
    possible_moves = []
    y, x = selected_piece
    piece = board[y][x]
    if piece!= 0 and piece%10==0:
        possible_moves = white_possible_moves(board, selected_piece)
        
        king_position = [0, 0]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 10:
                    king_position = [row, col]  

        if white_is_check(board, king_position):
            new_possible_moves = []
            for move in possible_moves:
                temp_board = copy.deepcopy(board)

                temp_board = black_move(temp_board, selected_piece, (move[0], move[1]))
                if piece == 10:
                    for king_move in possible_moves:
                        if white_is_check(temp_board, king_move) == False:
                            new_possible_moves.append(king_move)

                elif white_is_check(temp_board, king_position) == False:
                    new_possible_moves.append(move)
            
            possible_moves = new_possible_moves
        
    
        moves_to_remove = []        
        for piece_move in possible_moves:
            temp_board = copy.deepcopy(board)
            temp_board = black_move(temp_board, selected_piece, (piece_move[0], piece_move[1]))
            
            if white_is_check(temp_board, king_position) == True and piece != 10:
                moves_to_remove.append(piece_move)
            elif piece == 10:
                if white_is_check(temp_board, piece_move) == True:
                    moves_to_remove.append(piece_move)

        for move in moves_to_remove:
            possible_moves.remove(move)
            
        if piece == 10 and [7, 2] in possible_moves and [7, 3] not in possible_moves:
            possible_moves.remove([7, 2])
            
        if piece == 10 and [7, 6] in possible_moves and [7, 5] not in possible_moves:
            possible_moves.remove([7, 6])
        

    elif piece != 0:
        
        possible_moves = black_possible_moves(board, selected_piece)
        
        king_position = [0, 0]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 11:
                    king_position = [row, col] 
        
        if black_is_check(board, king_position):
            new_possible_moves = []
            for move in possible_moves:
                temp_board = copy.deepcopy(board)

                temp_board = black_move(temp_board, selected_piece, (move[0], move[1]))
                if piece == 11:
                    for king_move in possible_moves:
                        if black_is_check(temp_board, king_move) == False:
                            new_possible_moves.append(king_move)

                elif black_is_check(temp_board, king_position) == False:
                    new_possible_moves.append(move)
            
            possible_moves = new_possible_moves
        
    
        moves_to_remove = []        
        for piece_move in possible_moves:
            temp_board = copy.deepcopy(board)
            temp_board = black_move(temp_board, selected_piece, (piece_move[0], piece_move[1]))
            
            if black_is_check(temp_board, king_position) == True and piece != 11:
                moves_to_remove.append(piece_move)
            elif piece == 11:
                if black_is_check(temp_board, piece_move) == True:
                    moves_to_remove.append(piece_move)

        for move in moves_to_remove:
            possible_moves.remove(move)

        if piece == 11 and [0, 2] in possible_moves and [0, 3] not in possible_moves:
            possible_moves.remove([0, 2])
            
        if piece == 11 and [0, 6] in possible_moves and [0, 5] not in possible_moves:
            possible_moves.remove([0, 6])
              
    return possible_moves

def move(board, selected_piece, selected_square, turn):
    if turn % 10 == 0:
        white_real_move(board, selected_piece, selected_square)
    else:
        black_real_move(board, selected_piece, selected_square)
        
    return board

def white_move(board, selected_piece, selected_square):
    piece = board[selected_piece[0]][selected_piece[1]]
        
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board

def white_real_move(board, selected_piece, selected_square):
    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 10:
        
        #improve caste so that it can't be done when a piece is checked
        if initial_state.white_king_moved == 0 and selected_square == (7, 2) and initial_state.white_rook1_moved == 0:
            if white_is_check(board, [7, 2]) or white_is_check(board, [7, 3]) or white_is_check(board, [7, 4]):
                pass
            else:
                initial_state.white_king_moved = 1
                initial_state.white_rook1_moved = 1
                board[7][0] = 0
                board[7][3] = 50

          
        if initial_state.white_king_moved == 0 and selected_square == (7, 6) and initial_state.white_rook2_moved == 0:
            if white_is_check(board, [7, 6]) or white_is_check(board, [7, 5]) or white_is_check(board, [7, 4]):
                pass
            else:
                initial_state.white_king_moved = 1
                initial_state.white_rook2_moved = 1
                board[7][7] = 0
                board[7][5] = 50
    
    if piece == 50 and selected_piece == (7, 0):
        initial_state.white_rook1_moved = 1
    
    if piece == 50 and selected_piece == (7, 7):
        initial_state.white_rook2_moved = 1
        
    
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board


def black_move(board, selected_piece, selected_square):
    
    piece = board[selected_piece[0]][selected_piece[1]]
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board

def black_real_move(board, selected_piece, selected_square):
    
    piece = board[selected_piece[0]][selected_piece[1]]

    if piece == 11:
        
        #improve caste so that it can't be done when a piece is checked
        if initial_state.black_king_moved == 0 and selected_square == (0, 2) and initial_state.black_rook1_moved == 0:
            if black_is_check(board, [0, 2]) or black_is_check(board, [0, 3]) or black_is_check(board, [0, 4]):
                pass
            else:
                initial_state.black_king_moved = 1
                initial_state.black_rook1_moved = 1
                board[0][0] = 0
                board[0][3] = 51

          
        if initial_state.black_king_moved == 0 and selected_square == (0, 6) and initial_state.black_rook2_moved == 0:
            if black_is_check(board, [0, 6]) or black_is_check(board, [0, 5]) or black_is_check(board, [0, 4]):
               pass
            else:
                initial_state.black_king_moved = 1
                initial_state.black_rook2_moved = 1
                board[0][7] = 0
                board[0][5] = 51
    
    if piece == 51 and selected_piece == (0, 0):
        initial_state.black_rook1_moved = 1
    
    if piece == 51 and selected_piece == (0, 7):
        initial_state.black_rook2_moved = 1
        
    
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board