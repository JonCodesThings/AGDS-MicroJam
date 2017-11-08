from pygame import *

class Character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = Surface((40, 40))
        self.surface.fill(Color(255, 0, 0))
        self.yvelocity = 10
    def update(self, dt, input_):
        if (input_.getKeys()[K_UP]):
            self.y -= (1 * dt)
        elif (input_.getKeys()[K_DOWN]):
            self.y += (1 * dt)

        if (self.y < 200):
            self.y = 200

        if (self.y > 400):
            self.y = 400
            
        if (self.y < 300 and not input_.getKeys()[K_UP]):
            self.yvelocity = 5 * dt
            self.y += self.yvelocity

        if (self.y > 300 and not input_.getKeys()[K_DOWN]):
            self.yvelocity = 5 * dt
            self.y -= self.yvelocity

        if (self.y == 300):
            self.yvelocity = 0
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
