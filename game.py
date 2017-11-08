import sys, pygame
from pygame.locals import *
from Input import Input
from Character import Character
from NoteManager import NoteManager

if __name__ == "__main__":
    timer = 0
    gameover = False
    pygame.init()
    font_ = pygame.font.Font(None, 200)
    clock = pygame.time.Clock()
    character = Character(400, 300)
    note = NoteManager()
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
        note.update(clock.get_time())
        character.render(screen)
        note.render(screen)
        note.checkCollision(character, input_)
        score = font_.render("Score: " + str(character.getScore()), 0, pygame.Color(255, 255, 255))
        screen.blit(score, (0, 0))
        timer_out = font_.render("Time: " + str(300 - timer / 1000), 0, pygame.Color(255, 255, 255))
        screen.blit(timer_out, (0, 475))
        pygame.display.update()
        timer += clock.get_time()
        if (timer >= 300000):
            pygame.display.quit()
            sys.exit()
        clock.tick()
