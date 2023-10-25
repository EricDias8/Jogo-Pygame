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
        position_x = WIDTH/5
        position_y = HEIGHT/4
        position_width = WIDTH/2 + 100
        position_height = HEIGHT/2
        pygame.draw.rect(self.screen,WHITE,pygame.Rect(position_x,position_y,position_width,position_height))
        title = "SCORE:"
        tx = Text(None, 40, title, BLACK, (position_x + position_width/2, position_y + 20))
        tx.draw_center()
        for i in range(self.max_page):
            try:
                text = self.allscore[i + self.max_page*self.page].split(";")
                strout = 0
                tx = Text(None, 30, strout, BLACK, (position_x + position_width/2, position_y + 100 + 25*i))
                tx.draw_center()
            except:
                break
            