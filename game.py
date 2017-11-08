import sys, pygame
from pygame.locals import *
from Input import Input

if __name__ == "__main__":
    pygame.init()
    input_ = Input()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("whitebear")
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                sys.exit()
        input_.update()
