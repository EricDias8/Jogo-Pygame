import pygame, sys
from pygame.locals import *
from src.settings import *
from src.text import Text
from src.score import Score
from src.button import Button

def div_string(string,max_width):
    words = string.split()
    line = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1<= max_width:
            current_line += " " + word if current_line else word
        else:
            line.append(current_line)
            current_line = word
    if current_line:
        words.append(current_line)
    return line

class Menu():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.active = True
        self.state = 1
        self.fullscreen = False
        self.music = True
        self.player_name = ""
        self.score = Score()
        with open("playerName.txt") as f:
            contents = f.read()
            self.player_name = contents
        self.title = Text(None, 80, "Earthquake Escape", WHITE, [(WIDTH/2),(HEIGHT/2) - 250])
        self.sub = Text(None,30, "Press ENTER to Start the game", WHITE, [(WIDTH/2) - 140, HEIGHT - 200])
        self.name = Text(None, 30, "Hello" + self.player_name + "!",WHITE,[10, HEIGHT - 30])        
        self.btn_play = Button("White", (WIDTH/2) - 125, 320, "Play", self.next_scene)
        self.btn_options = Button("White", (WIDTH/2) - 125, 320, "Options", self.scene_options)
        self.btn_comand = Button("White", (WIDTH/2) - 125, 320, "Play", self.comand)
        self.btn_score = Button("White", (WIDTH/2) - 125, 320, "Play", self.score_scene)
        self.btn_quit = Button("White", (WIDTH/2) - 125, 640, "QUIT", self.quit_scene)
        self.btn_screen = Button("White", (WIDTH/2) - 125, 480, "FULL Screen: OFF", self.screen_change)
        self.btn_mute = Button("White", (WIDTH/2) - 125, 320, "Music: ON", self.mute)
        self.btn_back = Button("White", (WIDTH/2) - 125, 640, "Back", self.back)
        self.btn_nextPage = Button("White", (WIDTH/2) + 100, HEIGHT - 250, "->", self.next_page)
        self.btn_backPage = Button("White", (WIDTH/2) - 380, HEIGHT - 250, "<-", self.back_page)

        def next_scene(self):
            from src.game import Game
            game = Game()
            game.run()
            self.active = False

        def scene_options(self):
            self.state = 3

        def comand(self):
            self.state = 4

        def score_scene(self):
            self.state = 5

        def quit_game(self):
            pygame.quit()
            sys.exit()

        def screen_change(self):
            if(self.fullscreen == False):
                self.fullscreen = True
                self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Full Screen: ON",self.screen_change)
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        def mute(self):
            if(self.music):
                Music.stop()
                self.btn_mute = Button("white", (WIDTH/2) -125, 560, "Music: OFF", self.mute)
                self.music = False
            else:
                Music.play(-1)
                self.btn_mute = Button("white", (WIDTH/2) -125, 560, "Muisic: ON", self.mute)
                self.music = True
        def back(self):
            self.state = 2
            self.score.page = 0

        
        



