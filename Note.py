from pygame import *

class Note:
    def __init__(self, x, y, char):
        self.font_ = font.Font(None, 50)
        self.x = x
        self.y = y
        self.char = char
        self.surface = Surface((40, 40))
        self.surface.fill(Color(0, 0, 255))
        self.text_surface = self.font_.render(" " + char, 0, Color(255, 255, 255))
        self.isAlive = False
        self.AABB = Rect(x, y, 40, 40)
    def getSurface(self):
        return self.surface
    def getChar(self):
        return self.char
    def setChar(self, char):
        self.char = char
        self.surface.fill(Color(0, 0, 255))
        self.text_surface = self.font_.render(" " + char, 0, Color(255, 255, 255))
    def setAlive(self, alive):
        self.isAlive = alive
    def getAlive(self):
        return self.isAlive
    def getAABB(self):
        return self.AABB
    def update(self, dt):
        self.x += 0.25 * dt
        if (self.x + 40 >= 800):
            self.isAlive = False
        self.AABB.left = self.x
        self.AABB.top = self.y
    def render(self, screen):
        self.surface.blit(self.text_surface, (0,0))
        screen.blit(self.surface, (self.x, self.y))
