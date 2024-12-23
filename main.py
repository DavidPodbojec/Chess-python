import pygame
from calculate import calculate

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

def draw_grid(board, selected):
    global possible_moves
    
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL
            y = row * CELL

            piece = board[row][col]
 
            color = BLACK
            if (row + col) % 2 == 0:
                color = WHITE
                
            if (col * 100) < selected[0] < ((col+1) * 100) and (row * 100) < selected[1] < ((row + 1) * 100) and board[row][col] != 0:
                selected_square = (row, col)
                print(selected_square)                
            
                
            if board[row][col] != 0 and (col * 100) < selected[0] < ((col+1) * 100) and (row * 100) < selected[1] < ((row + 1) * 100):
                
                #selected = (y, x)
                selected_piece = (row, col)
                selected_square = (row, col)
                print(selected_piece)
                if piece % 10 == TURN:
                    possible_moves = calculate(board, selected_piece)

                if color == WHITE:
                    color = SHADED_WHITE
                else:
                    color = SHADED_BLACK            

            pygame.draw.rect(screen, color, (x, y, CELL, CELL))
            
            if piece != 0:
                piece_images[piece] = pygame.transform.scale(piece_images[piece], (CELL, CELL))

                screen.blit(piece_images[piece], (col * CELL, row * CELL))
            
            
            if [row, col] in possible_moves:
                pygame.draw.circle(screen, (80, 80, 80), ((col * CELL)+(CELL/2), (row * CELL)+(CELL/2)), 20)
                
            

            



selected = (0, 0)

board = [[0 for x in range(8) ] for i in range(8)]
    
board[0] = [51,41,31,21,11,31,41,51]
board[1] = [61 for i in range(8)]

board[6] = [60 for i in range(8)]
board[7] = [50,40,30,20,10,30,40,50]
                
while running:
    clicked = False
    mouse_x, mouse_y = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                selected = (mouse_x, mouse_y)
                clicked = True

    screen.fill("white")

    draw_grid(board, selected)

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()
