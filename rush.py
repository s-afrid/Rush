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
            self._event_check()
            # Update car position
            self.car.update_car()
            # Update the screen.
            self._update_window()

    def _event_check(self):
        """Function to handle keyboard and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.car.move_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.car.move_right = False

    def _update_window(self):
        """Funtion to handle screen updates"""
        # Set background
        self.window.blit(self.setting.bg,self.setting.bg.get_rect())
        # Draw car on the screen
        self.car.blitme()
        # Update the display.
        pygame.display.update()

if __name__ == "__main__":
    rush = Rush()
    rush.run_game()

        