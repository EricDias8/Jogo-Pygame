import pygame, sys
from pygame.locals import *
from src.settings import *
from src.text import Text
from src.button import Button
from src.score import Score

class Gameover():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.active = True
        self.title = Text(None, 60, "GAMEOVER", WHITE, [(WIDTH/2) - 125, (HEIGHT/2) - 270])
        self.btn_menu = Button("white", (WIDTH/2) - 250, HEIGHT - 100, "Menu", self.next_scene)
        self.btn_quit = Button("white", (WIDTH/2) + 50, HEIGHT - 100, "Sair", self.quit_game)
        self.score = Score()
        self.btn_next = Button("white", (WIDTH/2) + 100, HEIGHT - 250, "=>", self.score.next_page)
        self.btn_back = Button("white", (WIDTH/2) - 380, HEIGHT - 250, "<=", self.score.back_page)

    def next_scene(self):
        from src.menu import Menu
        menu = Menu()
        menu.run()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.active:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.quit_game()

                self.btn_next.events(event)
                self.btn_back.events(event)
                self.btn_menu.events(event)
                self.btn_quit.events(event)

            self.screen.fill(BLACK)
            self.title.drawFade()
            
            self.score.run()
            
            self.btn_back.draw()
            self.btn_next.draw()
            self.btn_menu.draw()
            self.btn_quit.draw()

            pygame.display.flip()
            FPSclock.tick(30)