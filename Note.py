from pygame import *

class Note:
    def __init__(self, x, y, char):
        font_ = font.Font(None, 16)
        self.x = x
        self.y = y
        self.char = char
        self.surface = Surface((40, 40))
        self.text_surface = font_.render(char, 0, Color(255, 255, 255))
    def render(self, screen):
        self.surface.blit(self.text_surface, (0,0))
        screen.blit(self.surface, (self.x, self.y))
