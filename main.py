import pygame
import time
from calculate import calculate, move, white_is_checkmate, black_is_checkmate

pygame.init()

WINDOW_SIZE = 800
GRID_SIZE = 8
CELL = WINDOW_SIZE / GRID_SIZE

WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

SHADED_WHITE = (172, 156, 130)
SHADED_BLACK = (130, 98, 71)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()
running = True

WHITE_TURN = 0
BLACK_TURN = 1

TURN = WHITE_TURN


piece_images = {
    10: pygame.image.load("images/white_king.png"),
    20: pygame.image.load("images/white_queen.png"),
    30: pygame.image.load("images/white_bishop.png"),
    40: pygame.image.load("images/white_knight.png"),
    50: pygame.image.load("images/white_rook.png"),
    60: pygame.image.load("images/white_pawn.png"),
     
    11: pygame.image.load("images/black_king.png"),
    21: pygame.image.load("images/black_queen.png"),
    31: pygame.image.load("images/black_bishop.png"),
    41: pygame.image.load("images/black_knight.png"),
    51: pygame.image.load("images/black_rook.png"),
    61: pygame.image.load("images/black_pawn.png")
}

selected_piece = (0, 0)
selected_square = (0, 0)
possible_moves = []

is_piece_selected = False

def checkmate(turn):
    font_size = 64
    font = pygame.font.SysFont(None, font_size)
    text = "WHITE lost" if turn == WHITE_TURN else "BLACK lost"
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
    
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()        
    

def draw_grid(board, selected):
    global possible_moves
    global is_piece_selected
    global selected_piece
    global TURN
    global is_checkmate
    
    is_checkmate = False
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL
            y = row * CELL

            piece = board[row][col]
 
            color = BLACK   
            if (row + col) % 2 == 0:
                color = WHITE
            
            if board[row][col] != 0 and (col * 100) < selected[0] < ((col+1) * 100) and (row * 100) < selected[1] < ((row + 1) * 100):
                
                #selected = (y, x)
                
                if piece % 10 == TURN:
                    selected_piece = (row, col)
                    possible_moves = calculate(board, selected_piece)
                    
                    is_piece_selected = True
                    
                    if color == WHITE:
                        color = SHADED_WHITE
                    else:
                        color = SHADED_BLACK

                 
            
            #work on this
            if (col * 100) < selected[0] < ((col+1) * 100) and (row * 100) < selected[1] < ((row + 1) * 100):
                selected_square = (row, col)
                
                if is_piece_selected and board[selected_piece[0]][selected_piece[1]] % 10 == TURN:
                    
                    if [selected_square[0], selected_square[1]] in possible_moves:
                        board = move(board, selected_piece, selected_square, TURN)
                        possible_moves = []
                        
                        if TURN == 0:
                            TURN = 1
                        else:
                            TURN = 0
                            
                        is_checkmate = False
                        
                        black_king_position = [0, 0]
                        white_king_position = [0, 0]
                        for row in range(len(board)):
                            for col in range(len(board[row])):
                                if board[row][col] == 11:
                                    black_king_position = [row, col]
                                if board[row][col] == 10:
                                    white_king_position = [row, col]
                        
                        if black_is_checkmate(board, black_king_position):
                            is_checkmate = True 

                        if white_is_checkmate(board, white_king_position):
                            is_checkmate = True
                            
                        is_piece_selected = False   
            
                
                    
                    
                          

            pygame.draw.rect(screen, color, (x, y, CELL, CELL))
            
            if piece != 0:
                piece_images[piece] = pygame.transform.scale(piece_images[piece], (CELL, CELL))

                screen.blit(piece_images[piece], (col * CELL, row * CELL))
            
            
            if [row, col] in possible_moves:
                color = SHADED_BLACK
                if (row + col) % 2 == 0:
                    color = SHADED_WHITE
                    
                #if opposite is to be captured
                if board[row][col] != 0 and board[row][col] != TURN:
                    pygame.draw.circle(screen, color, ((col * CELL)+(CELL/2), (row * CELL)+(CELL/2)), CELL/2, 10)
                else:
                    pygame.draw.circle(screen, color, ((col * CELL)+(CELL/2), (row * CELL)+(CELL/2)), 20)          
                    
    return (is_checkmate, TURN)             

selected = (0, 0)

board = [[0 for x in range(8) ] for i in range(8)]
    
board[0] = [51,41,31,21,11,31,41,51]
board[1] = [61 for i in range(8)]

board[6] = [60 for i in range(8)]
board[7] = [50,40,30,20,10,30,40,50]
                
while running:
    mouse_x, mouse_y = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                selected = (mouse_x, mouse_y)
                

    screen.fill("white")

    is_checkmate, TURN = draw_grid(board, selected)

    pygame.display.flip()
    if is_checkmate:
        checkmate(TURN)
    
    clock.tick(60) 

pygame.quit()
