import sys
import pygame
from setting import Settings
from car import Car


class Rush:
    """Class that handles game behaviour and assets."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.setting = Settings()
        self.window = pygame.display.set_mode((
            self.setting.width, self.setting.height))
        pygame.display.set_caption("Rush")
        # Car object
        self.car = Car(self)
    def run_game(self):
        """Run the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Draw car on the screen
            self.car.blitme()
            # Update the display.
            pygame.display.update()

if __name__ == "__main__":
    rush = Rush()
    rush.run_game()

        