import pygame
import sys
from config import piece_images, screen, WINDOW_SIZE, CELL, WHITE, BLACK

# Initialize the clock for managing frame rate
clock = pygame.time.Clock()

def promotion_popup(turn, board):
    """
    Displays a promotion popup allowing the player to select a piece for promotion.
    This function draws the entire board and a shaded popup for promotion.

    Parameters:
        turn (int): The current turn (0 for White, 1 for Black).
        board (list): The current state of the chessboard.

    Returns:
        int: The selected piece code for promotion.
    """
    promotion_running = True
    options = [20, 50, 30, 40] if turn == 0 else [21, 51, 31, 41]
    option_rects = []
    selected_option = None  # To track the currently selected option

    # Create a semi-transparent overlay for the popup
    overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
    overlay.set_alpha(150)  # Set transparency level (0-255)
    overlay.fill((0, 0, 0))  # Fill with black to create a shaded effect

    # Define the rectangle for the popup area
    popup_rect = pygame.Rect(WINDOW_SIZE // 4, 150, WINDOW_SIZE // 2, 200)  # Adjust position and size

    while promotion_running:
        # First, draw the board
        for row in range(len(board)):
            for col in range(len(board[row])):
                x, y = col * CELL, row * CELL
                color = WHITE if (row + col) % 2 == 0 else BLACK

                # Draw square
                pygame.draw.rect(screen, color, (x, y, CELL, CELL))

                # Draw piece if present
                piece = board[row][col]
                if piece != 0:
                    piece_image = pygame.transform.scale(piece_images[piece], (CELL, CELL))
                    screen.blit(piece_image, (x, y))

        # Draw the shaded overlay
        screen.blit(overlay, (0, 0))

        # Draw the popup background (solid rectangle)
        pygame.draw.rect(screen, (211, 176, 140), popup_rect)  # Black background for the popup
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 5)  # White border around the popup

        # Draw the popup text
        font = pygame.font.SysFont(None, 48)
        text = font.render("Promote to:", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_SIZE // 2, 150 + 50))
        screen.blit(text, text_rect)

        # Draw the promotion options inside the rectangle
        option_rects = []
        for i, piece in enumerate(options):
            x = popup_rect.x + (i * 100) + 10  # Adjusted x-coordinate inside popup
            y = popup_rect.y + 70  # Adjusted y-coordinate inside popup
            piece_image = pygame.transform.scale(piece_images[piece], (80, 80))
            option_rect = pygame.Rect(x, y, 80, 80)
            option_rects.append(option_rect)

            # Draw a border if this option is selected
            if selected_option == i:
                pygame.draw.rect(screen, (255, 0, 0), option_rect, 5)  # Red border for selected option

            screen.blit(piece_image, (x, y))

        # Event handling for the popup
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        selected_option = i  # Set selected option
                        # Wait until the player clicks to confirm selection
                        return options[i]

        # Update display
        pygame.display.flip()
        clock.tick(60)

# Example usage (during a promotion scenario):
# promotion_popup(0, board)  # Call this when promotion is triggered
