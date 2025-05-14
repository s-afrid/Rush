import pygame

class Car:
    """Class that represents the car."""
    def __init__(self,rush_screen):
        self.screen = rush_screen.window
        self.screen_rect = rush_screen.window.get_rect()
        # Load image and get its rect
        self.image = pygame.image.load('images/car.png')
        # Resize car
        self.image = pygame.transform.scale(self.image,(90,120))
        self.rect = self.image.get_rect()
        # Start position of the on the screen
        self.rect.center = self.screen_rect.center
        self.rect.centery = 600
        # Movement flag
        self.move_right = False

    def update_car(self):
        """Update car location based on the movement flag"""
        if self.move_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the car on the screen."""
        self.screen.blit(self.image,self.rect)