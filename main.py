import pygame

# pygame setup
pygame.init()

WINDOW_SIZE = 800
GRID_SIZE = 8
CELL = WINDOW_SIZE / GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()
running = True

#temporary
WHITE_PIECE = (255, 0, 0)
BLACK_PIECE = (0, 0, 255)

def draw_grid(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL
            y = row * CELL
            
            color = BLACK
            if (row + col) % 2 == 0:
                color = WHITE

            pygame.draw.rect(screen, color, (x, y, CELL, CELL))

            piece = board[row][col]
            #TEMPORARY
            piece_color = color

            if piece != 0 and piece % 10 == 0:
                piece_color = WHITE_PIECE
            elif piece != 0:
                piece_color = BLACK_PIECE

            piece_x = x - 2 * CELL/3
            piece_y = y - 2 * CELL/3

            pygame.draw.rect(screen, piece_color, (piece_x, piece_y,2 * CELL / 3,2 * CELL / 3))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    board = [[0 for x in range(8) ] for i in range(8)]
    
    board[0] = [50,40,30,20,10,30,40,50]
    board[1] = [60 for i in range(8)]

    board[6] = [66 for i in range(8)]
    board[7] = [55,44,33,22,11,33,44,55]

    draw_grid(board)

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()
