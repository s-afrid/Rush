import sys
import pygame

class Rush:
    """Class that handles game behaviour and assets."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rush")
    def run_game(self):
        """Run the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update the display.
            pygame.display.update()

if __name__ == "__main__":
    rush = Rush()
    rush.run_game()

        