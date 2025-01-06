import pygame

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

WINDOW_SIZE = 800
GRID_SIZE = 8
CELL = WINDOW_SIZE / GRID_SIZE

WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

SHADED_WHITE = (172, 156, 130)
SHADED_BLACK = (130, 98, 71)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

WHITE_TURN = 0
BLACK_TURN = 1

TURN = WHITE_TURN