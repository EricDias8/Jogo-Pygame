import pygame
from src.text import Text
from src.settings import *

def dividir_string(string, largura_maxima):
        palavras = string.split()
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            if len(linha_atual) + len(palavra) + 1 <= largura_maxima:
                linha_atual += " " + palavra if linha_atual else palavra
            else:
                linhas.append(linha_atual)
                linha_atual = palavra
        
        if linha_atual:
            linhas.append(linha_atual)
        return linhas

class Textbox():
    def __init__(self):
        self.active = False
        self.choiceMade = False
        self.screen = pygame.display.get_surface()
        self.width = WIDTH/2
        self.height = HEIGHT/3
        self.x = (WIDTH/2) - self.width/2
        self.y = 100
        self.arrow = pygame.image.load("assets/arrow.png")
        self.arrow = pygame.transform.scale(self.arrow, (18, 20))
        self.esc = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = WHITE
        self.text = ""
        
    def run(self):
        while self.active:                    
            self.draw()

    def change_esc(self):
        if self.esc < 0:
            self.esc = len(self.options) - 1
        elif self.esc >= len(self.options):
            self.esc = 0 

    def events(self, event):
        pass
            
    def draw(self):
        line_color = ARROZ
        line_width = 5
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.line(self.screen, line_color, (self.x, self.y), (self.x + self.width, self.y), line_width)
        pygame.draw.line(self.screen, line_color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), line_width)
        pygame.draw.line(self.screen, line_color, (self.x, self.y), (self.x, self.y + self.height), line_width)
        pygame.draw.line(self.screen, line_color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), line_width)
        lines = dividir_string(self.message, self.width/12 - 8)
        
        
        for i, line in enumerate(lines):
            tx = Text(None, 40, line, BLACK, (self.x + 10, self.y + 15 + i * 25))
            tx.draw()
       
        for i, option in enumerate(self.options):
            tx = Text(None, 35, option, BLACK, (self.x + 20 + (i/(len(self.options) - 1))*(self.width - 100), self.y + self.height - 40))
            tx.draw()
        self.screen.blit(self.arrow, (self.x + 5 + (self.esc / (len(self.options) - 1))*(self.width - 100), self.y + self.height - 40))
        return self.esc
    
    def getChoice(self):
        self.active = False
        self.choiceMade = True
        return self.options[self.esc]

    def defineOption(self, text):
        if(text == "table"):
            self.message = "You want to hide under a table in this room?"
            self.options = ["Yes", "No"]
        if(text == "stairs"):
            self.message = "Want to take the stairs?"
            self.options = ["Yes", "No"]
        if(text == "elevator"):
            self.message = "Do you want to take the elevator?"
            self.options = ["Yes", "No"]
        if(text == "fase-1"):
            self.message = "An earthquake just happened! You will have 30 seconds to take action!"
            self.options = ["Continue", "OK"]
        if(text == "fase-4"):
            self.message = "The earthquake has stopped, choose quickly, do you want to take the elevator or the stairs"
            self.options = ["Continue", "OK"]
        if(text == "fase-3-correct"):
            self.message = "Correct choice! Even with options to escape, the idea is to hide under a table until you stop"
            self.options = ["Continue", "OK"]
        if(text == "fase-1-correct"):
            self.message = "Choose Correct! In the middle of an earthquake, the ideal is to hide under a covered place like a table to protect you from things that could fall on your head."
            self.options = ["Continue", "OK"]
        if(text == "fase-2-correct"):
            self.message = "Choose Correct! During an earthquake, windows can break and end up injuring you."
            self.options = ["Continue", "OK"]
        if(text == "fase-2-incorrect"):
            self.message = "Incorrect Choice! You need to evaluate objects before hiding. Windows can break and injure you during an earthquake. Lost a life."
            self.options = ["Continue", "OK"]
        if(text == "elevador-incorrect"):
            self.message = "Wrong!, during an earthquake You should not take an elevator, it can be risky. Lost a life"
            self.options = ["Continue", "OK"]
        if(text == "elevador-incorrect-2"):
            self.message = "Wrong! Even if the earthquake has stopped, it is not recommended to take the elevator. Lost a life"
            self.options = ["Continue", "OK"]
        if(text == "stairs-incorrect"):
            self.message = "Wrong!, during an earthquake You should not walk on stairs, it can be risky. Lost a life"
            self.options = ["Continue", "OK"]
        if(text == "stairs-correct"):
            self.message = "Perfect! You should avoid the elevator even after an earthquake."
            self.options = ["Continue", "OK"]
        if(text == "Time-ERROR"):
            self.message = "Time is up! lost a life!"
            self.options = ["Continue", "OK"]
        if(text == "END"):
            self.message = "Congratulations! You made all the right decisions and finished the game!"
            self.options = ["Continue", "OK"]
        else:
            "Choose an object to interact with"