from Note import Note
import random

class NoteManager:
    def __init__(self):
        random.seed()
        self.x = -20
        self.high_y = 161
        self.low_y = 439
        self.chars = ["z", "x", "c"]
        self.Notes = []
        self.timer = 0
        for i in range(0, 8):
            if (i % 2 == 0):
                note = Note(self.x, self.high_y, self.chars[random.randint(0,2)])
                self.Notes.append(note)
            else:
                note = Note(self.x, self.low_y, self.chars[random.randint(0,2)])
                self.Notes.append(note)

    def spawn(self):
        for i in self.Notes:
            if (not i.getAlive()):
                i.x = -20
                i.setChar(self.chars[random.randint(0,2)])
                i.setAlive(True)
                return None

    def render(self, screen):
        for i in self.Notes:
            if (i.getAlive()):
                i.render(screen)

    def update(self, dt):
        self.timer += dt
        for i in self.Notes:
            if (i.getAlive()):
                i.update(dt)
        if (self.timer >= 2500):
            self.timer = 0
            self.spawn()
            
    def checkCollision(self, player, input_):
        for i in self.Notes:
            if(i.getAlive()):
                player.NoteCollide(i, input_)
