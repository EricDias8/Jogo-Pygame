import pygame, sys
from src.text import Text
from src.settings import *
from pygame.locals import *

class Timer():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time = 0 
        self.font = pygame.font.Font(None, 40)
        self.screen = pygame.display.get_surface()

    def draw(self, sec):
        self.time = int(sec)
        text_content = str(self.time)
        text_surface = self.font.render(text_content, True,(255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)
        self.screen.blit(text_surface,text_rect)

class UI():
    def __init__(self):
        self.screen = pygame.display.get_surface()
    
    def run(self, seconds, PlayerLife):
        text_timer = Text(None, 35, "TIMER:", RED, [30,30])
        text_surface = Text(None, 30, seconds, RED, [100, 30])
        player_life_text = Text(None, 30, "LIFE:", RED, [30, HEIGHT - 50])
        player_life = Text(None, 30, str(PlayerLife), RED, [100, HEIGHT - 50])
        text_timer.draw()
        text_surface.draw()
        player_life_text.draw()
        player_life.draw()
