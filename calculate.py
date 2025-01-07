from possible_moves import white_possible_moves, black_possible_moves
from check import white_is_check, black_is_check
from move import white_real_move, black_real_move
import copy
import initial_state

def move_piece(board, selected_piece, selected_square):
    
    piece = board[selected_piece[0]][selected_piece[1]]
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board

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

                temp_board = move_piece(temp_board, selected_piece, (move[0], move[1]))
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
            temp_board = move_piece(temp_board, selected_piece, (piece_move[0], piece_move[1]))
            
            if white_is_check(temp_board, king_position) == True and piece != 10:
                moves_to_remove.append(piece_move)
            elif piece == 10:
                if white_is_check(temp_board, piece_move) == True:
                    moves_to_remove.append(piece_move)
        
        for move in moves_to_remove:
            possible_moves.remove(move)
            
        if piece == 10 and [7, 2] in possible_moves and [7, 3] not in possible_moves and initial_state.white_king_moved == 0:
            possible_moves.remove([7, 2])
            
        if piece == 10 and [7, 6] in possible_moves and [7, 5] not in possible_moves and initial_state.white_king_moved == 0:
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

                temp_board = move_piece(temp_board, selected_piece, (move[0], move[1]))
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
            temp_board = move_piece(temp_board, selected_piece, (piece_move[0], piece_move[1]))
            
            if black_is_check(temp_board, king_position) == True and piece != 11:
                moves_to_remove.append(piece_move)
            elif piece == 11:
                if black_is_check(temp_board, piece_move) == True:
                    moves_to_remove.append(piece_move)

        for move in moves_to_remove:
            possible_moves.remove(move)

        if piece == 11 and [0, 2] in possible_moves and [0, 3] not in possible_moves and initial_state.black_king_moved == 0:
            possible_moves.remove([0, 2])
            
        if piece == 11 and [0, 6] in possible_moves and [0, 5] not in possible_moves and initial_state.black_king_moved == 0:
            possible_moves.remove([0, 6])
              
    return possible_moves

def move(board, selected_piece, selected_square, turn):
    if turn % 10 == 0:
        white_real_move(board, selected_piece, selected_square)
    else:
        black_real_move(board, selected_piece, selected_square)
        
    return board



