import sys, pygame
from pygame.locals import *
from Input import Input
from Character import Character
from Note import Note

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    character = Character(400, 300)
    input_ = Input()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("whitebear")
    clock.tick()
    while (True):
        screen.fill(pygame.Color(0, 0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                sys.exit()
        input_.update()
        character.update(clock.get_time(), input_)
        character.render(screen)
        pygame.display.update()
        clock.tick()
