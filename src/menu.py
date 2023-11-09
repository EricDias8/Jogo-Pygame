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
        with open('playerName.txt') as f:
            contents = f.read()
            self.player_name = contents
        self.title = Text(None, 60, "Earthquake Escape", WHITE, [(WIDTH/2), (HEIGHT/2) - 250])
        self.sub = Text(None, 31, "Press ENTER to play", WHITE, [(WIDTH/2) - 140, HEIGHT - 200])
        self.name = Text(None, 41, "Welcome " + self.player_name + " to the game!!", WHITE, [(WIDTH/2) - 200, (HEIGHT/2) - 190])
        self.btn_play = Button("white", (WIDTH/2) - 125, 320, "PLAY", self.next_scene)
        self.btn_options = Button("white", (WIDTH/2) - 125, 400, "Option", self.scene_options)
        self.btn_comandos = Button("white", (WIDTH/2) - 125, 480, "Description", self.comandos)
        self.btn_score = Button("white", (WIDTH/2) - 125, 560, "Score", self.score_scene)
        self.btn_quit = Button("white", (WIDTH/2) - 125, 640, "QUIT", self.quit_game)
        self.btn_screen = Button("white", (WIDTH/2) - 125, 380, "Full Screen: OFF", self.screen_change)
        self.btn_mute = Button("white", (WIDTH/2) - 125, 460, "Music: ON", self.mute)
        self.btn_back = Button("white", (WIDTH/2) - 125, 640, "Back", self.back)
        self.btn_nextPage = Button("white", (WIDTH/2) + 100, HEIGHT - 250, "->", self.score.next_page)
        self.btn_backPage = Button("white", (WIDTH/2) - 380, HEIGHT - 250, "<-", self.score.back_page)

    def mute(self):
        if(self.music):
            Music.stop()
            self.btn_mute = Button("white", (WIDTH/2) - 125, 460, "Music: OFF", self.mute)
            self.music = False
        else:
            Music.play(-1)
            self.btn_mute = Button("white", (WIDTH/2) - 125, 460, "Music: ON", self.mute)
            self.music = True

    def back(self):
        self.state = 2
        self.score.page = 0

    def screen_change(self):
        if(self.fullscreen == False):
            self.fullscreen = True
            self.btn_screen = Button("white", (WIDTH/2) - 125, 380, "Full Screen: ON", self.screen_change)
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            self.fullscreen = False
            self.btn_screen = Button("white", (WIDTH/2) - 125, 380, "Full Screen: OFF", self.screen_change)
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
    def scene_options(self):
        self.state = 3

    def score_scene(self):
        self.state = 5
    
    def comandos(self):
        self.state = 4

    def next_scene(self):
        from src.game import Game
        game = Game()
        game.run()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.active:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if self.state == 1:
                        if event.key == pygame.K_RETURN:
                            self.state = 2
                if self.state == 2:
                    self.btn_play.events(event)
                    self.btn_options.events(event)
                    self.btn_comandos.events(event)
                    self.btn_score.events(event)
                    self.btn_quit.events(event)
                elif self.state == 3:
                    self.btn_screen.events(event)
                    self.btn_back.events(event)
                    self.btn_mute.events(event)
                elif self.state == 4:
                    self.btn_back.events(event)
                elif self.state == 5:
                    self.btn_nextPage.events(event)
                    self.btn_backPage.events(event)
                    self.btn_back.events(event)

            self.screen.fill(BLACK)
            self.title.draw_center()
            if self.state != 1:
                self.name.draw() 
            if self.state == 1:
                self.sub.drawFade()
            elif self.state == 2:
                
                self.btn_play.draw() 
                self.btn_comandos.draw()         
                self.btn_options.draw()
                self.btn_score.draw()         
                self.btn_quit.draw()
            elif self.state == 3:
                self.btn_screen.draw()
                self.btn_mute.draw()
                self.btn_back.draw()
            elif self.state == 4:
                position_x = WIDTH/5
                position_y = HEIGHT/3
                position_width = WIDTH/2 + 150
                position_height = HEIGHT/2
                pygame.draw.rect(self.screen, WHITE, pygame.Rect(position_x, position_y, position_width, position_height))
                title = "Comand:"
                description = "Sobre:"
                text = "Para movimentar o jogador precione os direcionais (setas) do teclado."
                text_2 = "Para interragir com objetos pressione a tecla 'Z' ou 'X' proximo a um objeto."
                desc = "Earthquake Escape é um jogo onde o jogador precissa realizar escolhas ao se encontrar em um desastre natural"
                tx = Text(None, 40, title, BLACK, (position_x + position_width/2 - 80, position_y + 15))
                tx.draw()
                tx = Text(None, 30, text, BLACK, (position_x + 10, position_y + 80))
                tx.draw()
                tx = Text(None, 30, text_2, BLACK, (position_x + 10, position_y + 110))
                tx.draw()
                tx = Text(None, 40, description, GRAY_2, (position_x + position_width/2 - 50, position_y + 140))
                tx.draw()
                lines = div_string(desc, position_width/12 - 1)
                for i, line in enumerate(lines):
                    tx = Text(None, 35, line, BLACK, (position_x + 10, position_y + 200 + i * 25))
                    tx.draw()
                self.btn_back.draw()
            elif self.state == 5:
                self.score.run()
                self.btn_back.draw()
                self.btn_backPage.draw()
                self.btn_nextPage.draw()
            pygame.display.flip()
            FPSclock.tick(30)
