import pygame

from src.text import Text
from src.settings import *

# Taken from the internet
# https://www.youtube.com/watch?app=desktop&v=G8MYGDf_9ho

class Button():
    def __init__(self, color, x, y, text, call_back):
        self.screen = pygame.display.get_surface()
        self.color = color
        self.rect = pygame.Rect(x, y, 250, 64)
        self.text = text
        self.text_color = GRAY_2 
        self.text_position = [(x + self.rect.width / 2), (y + self.rect.height / 2)]
        self.render = Text(None, 40, self.text, self.text_color, self.text_position)
        self.call_back = call_back

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = RED
                self.render.update_text(self.text, WHITE)
            else:
                self.color = WHITE
                self.render.update_text(self.text, GRAY)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.call_back()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.render.draw_center()