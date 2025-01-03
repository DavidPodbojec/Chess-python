from possible_moves import black_possible_moves, white_possible_moves
import copy

def move_piece(board, selected_piece, selected_square):
    
    piece = board[selected_piece[0]][selected_piece[1]]
    
    board[selected_piece[0]][selected_piece[1]] = 0
    board[selected_square[0]][selected_square[1]] = piece
    return board

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

