import pygame
from pygame.locals import *

from src.settings import *
from src.text import Text

class Score():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.allscore = ""
        self.page = 0
        self.max_page = 7
        with open('ranking.txt') as f:
            contents = f.read()
            self.allscore = contents.split("\n")

    def back_page(self):
        if(self.page >= 1):
            self.page -= 1

    def next_page(self):
        if(self.max_page *(self.page+1) < len(self.allscore)):
            self.page += 1

    def run(self):
        bx = WIDTH/5
        by = HEIGHT/4
        bwd = WIDTH/2 + 100
        bht = HEIGHT/2
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(bx, by, bwd, bht))
        titulo = "Score:"
        tx = Text(None, 40, titulo, BLACK, (bx + bwd/2, by + 20))
        tx.draw_center()
        for i in range(self.max_page):
            try:
                text = self.allscore[i+self.max_page*self.page].split(";")
                strout = "{}° {} | Tempo: {}s | Vida: {}".format(i+self.max_page*self.page + 1, text[0], text[1], text[2])
                tx = Text(None, 30, strout, BLACK, (bx + bwd/2, by + 100 + 25*i))
                tx.draw_center()
            except:
                break
            