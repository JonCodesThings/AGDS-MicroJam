from pygame import *

class Character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = Surface((40, 40))
        self.surface.fill(Color(255, 0, 0))
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
