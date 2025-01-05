import pygame
import sys

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

def promotion_popup(turn):
    """
    Display a popup for pawn promotion and return the selected piece.
    """
    promotion_running = True
    options = [20, 50, 30, 40] if turn == WHITE_TURN else [21, 51, 31, 41]  # Queen, Rook, Bishop, Knight
    selected_index = 0

    while promotion_running:
        # Draw popup
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Promote to:", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_SIZE // 2, 100))
        screen.blit(text, text_rect)

        # Draw options
        for i, piece in enumerate(options):
            x = (WINDOW_SIZE // 2 - 150) + i * 100
            y = 200
            if i == selected_index:
                pygame.draw.rect(screen, (255, 215, 0), (x - 5, y - 5, 90, 90), 3)  # Highlight
            piece_image = pygame.transform.scale(piece_images[piece], (80, 80))
            screen.blit(piece_image, (x, y))

        # Event handling for the popup
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    promotion_running = False
                    return options[selected_index]

        pygame.display.flip()
