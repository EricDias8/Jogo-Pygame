import pygame
from src.settings import *
from src.entername import inputName

# Start the pygame engine
pygame.init()
pygame.font.init()
pygame.display.set_caption('Earthquake Escape')
screen = pygame.display.set_mode([WIDTH,HEIGHT])

# Print the game started
print("System UP!")

if __name__ == "__main__":
    name = inputName()
    name.run()

