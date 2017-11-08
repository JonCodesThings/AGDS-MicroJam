import sys, pygame
from pygame.locals import *
from Input import Input
from Character import Character
from Note import Note

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    character = Note(400, 300, "n")
    input_ = Input()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("whitebear")
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                sys.exit()
        input_.update()
        character.render(screen)
        pygame.display.update()
