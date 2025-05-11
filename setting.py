import pygame
import math
class Settings:
    """Class representing settings of the game."""
    def __init__(self):
        self.width = 600
        self.height = 700
        self.bg = pygame.image.load('images/road.png')
        self.bg = pygame.transform.scale(self.bg,(self.width,self.height))

