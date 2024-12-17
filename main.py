import pygame

# pygame setup
pygame.init()

WINDOW_SIZE = 800
GRID_SIZE = 8
CELL = WINDOW_SIZE / GRID_SIZE

WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

SHADED_WHITE = (216, 195, 163)
SHADED_BLACK = (163, 122, 89)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()
running = True


piece_images = {
    10: pygame.image.load("images/white_king.png"),
    20: pygame.image.load("images/white_queen.png"),
    30: pygame.image.load("images/white_bishop.png"),
    40: pygame.image.load("images/white_knight.png"),
    50: pygame.image.load("images/white_rook.png"),
    60: pygame.image.load("images/white_pawn.png"),
     
    11: pygame.image.load("images/black_king.png"),
    22: pygame.image.load("images/black_queen.png"),
    33: pygame.image.load("images/black_bishop.png"),
    44: pygame.image.load("images/black_knight.png"),
    55: pygame.image.load("images/black_rook.png"),
    66: pygame.image.load("images/black_pawn.png")
}

def draw_grid(board, mouse_x, mouse_y):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL
            y = row * CELL

            #determine if mouse_x and y belong here
            
            color = BLACK
            if (row + col) % 2 == 0:
                color = WHITE

            pygame.draw.rect(screen, color, (x, y, CELL, CELL))

            piece = board[row][col]

            if piece != 0:
                piece_images[piece] = pygame.transform.scale(piece_images[piece], (CELL, CELL))
                screen.blit(piece_images[piece], (col * CELL, row * CELL))


                
while running:
    clicked = False
    mouse_x, mouse_y = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                clicked = True
                print(f"{mouse_x} , {mouse_y}")

    screen.fill("white")
    
    board = [[0 for x in range(8) ] for i in range(8)]
    
    board[0] = [50,40,30,20,10,30,40,50]
    board[1] = [60 for i in range(8)]

    board[6] = [66 for i in range(8)]
    board[7] = [55,44,33,22,11,33,44,55]

    draw_grid(board, mouse_x, mouse_y)

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()
