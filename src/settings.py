import pygame
pygame.mixer.init()

#Clock for the FPS
FPSclock = pygame.time.Clock()

#Screen
WIDTH = 1280
HEIGHT = 720

# colors
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAY = (51,51,51)
GRAY_2 = (114,114,114)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

Music = pygame.mixer.Sound("assets/MusicMenu.mp3")