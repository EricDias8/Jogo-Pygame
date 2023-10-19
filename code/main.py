# importando a biblioteca do pygame
import pygame, sys
# importando as configurações do meu jogo
from settings import *
# from debug import debug importar quando for utilizado
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		# nome da janela do jogo
		pygame.display.set_caption('Earthquake Escape')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		while True:
			# LOOP para o jogo rodar
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			# screen cor preta da tela junto com o update dela e depois o controle de FPS
            # debug('DEBUG') utilizamos para fazer o debug do jogo
			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()