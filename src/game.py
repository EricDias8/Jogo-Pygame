# Imports
import pygame, os, sys, random, pytmx, math
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# Modulos
from src.settings import *
from src.models.player import Player
from src.models.npc import Npc
from src.models.entity import Entity
from src.Display import UI
from src.interection import Textbox
from src.file import TextFile

class SpriteSheet():
    def __init__(self, img):
        self.sheet = img
    
    def get_image(self, x, y, width, height, scale, color):
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.sheet, (0, 0), ((x * width), (y * height), width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        img.set_colorkey(color)

        return img

class Game():
    def __init__(self):
        self.active = True
        self.life = 3
    def run(self, map = 1, life_map = 3, total_time = 0):
        screen = pygame.display.get_surface()
        spriteimg = pygame.image.load(os.path.join('assets','sprite.png')).convert_alpha()
        entitiesList = []
        sprite = SpriteSheet(spriteimg)
        player = Player(sprite, 600, 300, 10, 64, 70, 1)
        entitiesList.append(player)
        player.life = life_map
        desk = pygame.image.load(os.path.join('assets','desk.png')).convert_alpha()
        rectdesk = desk.get_rect()
        deskobj = Entity(desk, 300, 200, 0, rectdesk.width, rectdesk.height, 1, "level1")
        deskobj2 = Entity(desk, 800, 300, 0, rectdesk.width, rectdesk.height, 1, "level2")
        textbox = Textbox()
        spriteimgnpc = pygame.image.load(os.path.join('assets','npc.png')).convert_alpha()
        spritenpc = SpriteSheet(spriteimgnpc)
        spriteimgnpc2 = pygame.image.load(os.path.join('assets','npc2.png')).convert_alpha()
        spritenpc2 = SpriteSheet(spriteimgnpc2)
        npc = Npc(spritenpc, WIDTH/2, HEIGHT/2, 5, 32, 32, 1.7)
        npc2 = Npc(spritenpc2, WIDTH/2, HEIGHT/2, 5, 32, 32, 1.7)
        entitiesList.append(npc)
        entitiesList.append(npc2)
        area1 = Entity(desk, 70, 300, 0, 300, 180, 1, "level1")
        area2 = Entity(desk, 500, 450, 0, 200, 150, 1, "level1")
        area3 = Entity(desk, 500, 100, 0, 250, 150, 1, "level1")
        area4 = Entity(desk, 700, 150, 0, 300, 200, 1, "level1")
        area5 = Entity(desk, 950, 320, 0, 300, 200, 1, "level1")
        areaElevador  = Entity(desk, 300, 120, 0, 150, 150, 1, "level1")


        self.direcionarMenu = False
        textbox = Textbox()
        textFile = TextFile("ranking.txt")
        textFilePlayerName = TextFile("playerName.txt")
        player_name = textFilePlayerName.readTextFile()

        self.fase = map
        self.resposta = ""
        start_ticks=pygame.time.get_ticks() #starter tick
        self.ended = False
        ui = UI()
        self.time = 0
        self.max_time = 20
        self.next_stage = False

        player.time = total_time

        tmxdata_1 = load_pygame('map/lvlone.tmx')
        tmxdata_2 = load_pygame('map/lvltwo.tmx')
        tmxdata_3 = load_pygame('map/lvlthree.tmx')
        '''
        if self.fase == 2:
            area1.changeArea(0,0,area1.width, area1.height)
        '''
        self.continuar = 0
        self.paused = False
        if self.fase == 1:
            self.paused = True
            self.continuar = 5
            textbox.defineOption("fase-1")
            textbox.active = True
        if self.fase == 4:
            self.continuar = 5
            textbox.defineOption("fase-4")
            textbox.active = True
        if self.fase == 5:
            self.continuar = 5
            textbox.defineOption("fim")
            textbox.active = True
            self.direcionarMenu = True
        

        
        seconds = 0
    
        while self.active:
            screen.fill(BLACK)
            


            if(self.fase == 1):
                    
                imagenew = tmxdata_1.get_tile_image_by_gid
                for layer in tmxdata_1.visible_layers:
                    if isinstance(layer, pytmx.TiledTileLayer):
                        for x, y, gid, in layer:
                            tile = imagenew(gid)
                            if tile:
                                # Calculo do Thibas
                                calc_x = (math.sqrt(2) * tmxdata_1.width * x  - math.sqrt(2) * tmxdata_1.height * y ) / 0.885
                                calc_y =  (math.sqrt(2) * tmxdata_1.width * x  + math.sqrt(2) * tmxdata_1.height * y) / 1.77
                                # print(x, y)
                                if layer.name == "background":
                                    screen.blit(tile, (calc_x+610, calc_y+80))
                                else:
                                    screen.blit(tile, (calc_x+610, calc_y-20)) 
                                    melly = Entity(tile, (calc_x+635), (calc_y+70), 0, tile.get_width() - 40, tile.get_height() - 110, 1, "level1")
                                    #melly.DrawHitbox(screen)
                                    for i in range(len(entitiesList)):
                                        e = entitiesList[i]
                                        #e.DrawHitbox(screen)
                                        if(e.isColliding(melly)):
                                            e.colisao = True
                                            e.block()
                                        else:
                                            e.colisao = False
            elif(self.fase == 2):
                imagenew = tmxdata_2.get_tile_image_by_gid
                for layer in tmxdata_2.visible_layers:
                    if isinstance(layer, pytmx.TiledTileLayer):
                        for x, y, gid, in layer:
                            tile = imagenew(gid)
                            if tile:
                                # Calculo do Thibas
                                calc_x = (math.sqrt(2) * tmxdata_2.width * x  - math.sqrt(2) * tmxdata_2.height * y ) / 0.885
                                calc_y =  (math.sqrt(2) * tmxdata_2.width * x  + math.sqrt(2) * tmxdata_2.height * y) / 1.77
                                # print(x, y)
                                if layer.name == "background":
                                    screen.blit(tile, (calc_x+610, calc_y+80))
                                else:
                                    screen.blit(tile, (calc_x+610, calc_y-20)) 
                                    melly = Entity(tile, (calc_x+635), (calc_y+70), 0, tile.get_width() - 40, tile.get_height() - 110, 1, "level1")
                                    #melly.DrawHitbox(screen)
                                    for i in range(len(entitiesList)):
                                        e = entitiesList[i]
                                        #e.DrawHitbox(screen)
                                        if(e.isColliding(melly)):
                                            e.colisao = True
                                            e.block()
                                        else:
                                            e.colisao = False

            elif self.fase == 3 or self.fase == 4:
                imagenew = tmxdata_3.get_tile_image_by_gid
                for layer in tmxdata_3.visible_layers:
                    if isinstance(layer, pytmx.TiledTileLayer):
                        for x, y, gid, in layer:
                            tile = imagenew(gid)
                            if tile:
                                # Calculo do Thibas
                                calc_x = (math.sqrt(2) * tmxdata_3.width * x  - math.sqrt(2) * tmxdata_3.height * y ) / 0.885
                                calc_y =  (math.sqrt(2) * tmxdata_3.width * x  + math.sqrt(2) * tmxdata_3.height * y) / 1.77
                                # print(x, y)
                                if layer.name == "background":
                                    screen.blit(tile, (calc_x+610, calc_y+80))
                                else:
                                    screen.blit(tile, (calc_x+610, calc_y-20)) 
                                    melly = Entity(tile, (calc_x+635), (calc_y+70), 0, tile.get_width() - 40, tile.get_height() - 110, 1, "level1")
                                    #melly.DrawHitbox(screen)
                                    for i in range(len(entitiesList)):
                                        e = entitiesList[i]
                                        #e.DrawHitbox(screen)
                                        if(e.isColliding(melly)):
                                            e.colisao = True
                                            e.block()
                                        else:
                                            e.colisao = False
                
            
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    exit()

                #Key event Player
                if event.type == KEYDOWN and textbox.active == False:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == K_LEFT:
                        player.actualDirection = player.directions[0]
                        player.currentFrame = player.walkSpriteFrame[0]
                        player.left = True
                        player.cur_frame = 0
                    if event.key == K_RIGHT:
                        player.actualDirection = player.directions[2]
                        player.currentFrame = player.walkSpriteFrame[1]
                        player.right = True
                        player.cur_frame = 0
                    if event.key == K_UP:
                        player.actualDirection = player.directions[3]
                        player.up = True
                        player.cur_frame = 0
                    if event.key == K_DOWN:
                        player.actualDirection = player.directions[1]
                        player.down = True
                        player.cur_frame = 0
                    if event.key == K_z:
                        pos = player.getPlayerFront(screen)
                        if self.fase == 1:
                            if area1.checkHitBox(pos[0], pos[1]) or area2.checkHitBox(pos[0], pos[1]) or area3.checkHitBox(pos[0], pos[1]) or area4.checkHitBox(pos[0], pos[1]) or area5.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("mesa")
                                textbox.active = True
                        if self.fase == 2:
                            if area1.checkHitBox(pos[0], pos[1]) or area2.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("mesa")
                                textbox.active = True
                            if area3.checkHitBox(pos[0], pos[1]) or area4.checkHitBox(pos[0], pos[1]) or area5.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("mesa")
                                textbox.active = True
                        if self.fase == 3:
                            if area1.checkHitBox(pos[0], pos[1]) or area2.checkHitBox(pos[0], pos[1]) or area3.checkHitBox(pos[0], pos[1]) or area4.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("mesa")
                                textbox.active = True
                            if area5.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("escada")
                                textbox.active = True
                            if areaElevador.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("elevador")
                                textbox.active = True
                        if self.fase == 4:
                            if area5.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("escada")
                                textbox.active = True
                            if areaElevador.checkHitBox(pos[0], pos[1]):
                                textbox.defineOption("elevador")
                                textbox.active = True
                elif event.type == KEYDOWN and textbox.active == True:
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    if event.key == K_z:
                        self.resposta = textbox.getChoice()
                        if self.continuar == 1:
                            self.continuar = 2
                        elif self.continuar == 3:
                            self.continuar = 4
                        elif self.continuar == 5:
                            self.max_time = 20
                            textbox.active = False
                            self.continuar = 0
                            self.paused = False
                            start_ticks=pygame.time.get_ticks() 
                            if self.direcionarMenu == True:
                                self.continuar = 6
                        elif self.ended == True:
                            self.continuar = 6
                    if event.key == K_LEFT:
                        textbox.esc -= 1
                        textbox.change_esc()
                    if event.key == K_RIGHT:
                        textbox.esc += 1
                        textbox.change_esc()
                    
                if event.type == KEYUP and textbox.active == False:
                    if event.key == K_LEFT:
                        player.left = False
                        player.cur_frame = 0
                    elif event.key == K_RIGHT:
                        player.right = False
                        player.cur_frame = 0
                    elif event.key == K_UP:
                        player.up = False
                        player.cur_frame = 0
                    elif event.key == K_DOWN:
                        player.down = False
                        player.cur_frame = 0

            if(player.x < -20 ):
                player.x = -20
            if(player.x > WIDTH-100):
                player.x = WIDTH-100
            if(player.y < 0):
                player.y = 0
            if(player.y > HEIGHT-140):
                player.y = HEIGHT-140
                
            if textbox.choiceMade == True:
                if self.fase == 1:
                    if self.resposta == "Sim":
                        textbox.defineOption("fase-1-correto")
                        textbox.active = True
                        player.time += int(text_content)
                        self.next_stage = True
                        textbox.choiceMade = False
                        self.continuar = 1
                elif self.fase == 2:
                    if self.resposta == "Sim":
                        if area1.checkHitBox(pos[0], pos[1]) or area2.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("fase-2-correto")
                            textbox.active = True
                            player.time += int(text_content)
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 1
                        else:
                            textbox.defineOption("fase-2-incorreto")
                            textbox.active = True
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 3
                elif self.fase == 3:
                    if self.resposta == "Sim":
                        if areaElevador.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("elevador-incorreto")
                            textbox.active = True
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 3
                        elif area5.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("escada-incorreto")
                            textbox.active = True
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 3
                        else:
                            textbox.defineOption("fase-1-correto")
                            textbox.active = True
                            player.time += int(text_content)
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 1
                elif self.fase == 4:
                    if self.resposta == "Sim":
                        if areaElevador.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("elevador-incorreto-2")
                            textbox.active = True
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 3
                        if area5.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("escada-correto")
                            textbox.active = True
                            player.time += int(text_content)
                            self.next_stage = True
                            textbox.choiceMade = False
                            self.continuar = 1
                            self.ended = True

                    
            if self.continuar == 4:
                self.life -= 1
                self.run(self.fase, self.life, player.time)        
            elif (self.time > 20 and self.next_stage == False):
                textbox.defineOption("erro-tempo")
                textbox.active = True
                self.continuar = 3
            elif self.continuar == 0 and self.paused == False:
                seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            elif self.continuar == 2:
                self.fase += 1
                self.run(self.fase, self.life, player.time)
            elif self.continuar == 6:
                from src.menu import Menu
                menu = Menu()
                menu.run()
                self.active = False

            
                

            if self.life <= 0:
                from src.gameover import Gameover
                gameouver = Gameover()
                gameouver.run()

            npc.Draw(screen)
            npc2.Draw(screen) 
            player.Draw(screen)        


            if(textbox.active == True):
                textbox.draw()
            else:      
                player.block()
                player.Move()   

            npc.Move()
            npc2.Move()
            if self.ended == True:
                textFile.copyFileToTemp()
                textFile.readFile(player_name, str(player.time), str(player.life))
                
                self.ended = False

            self.time = int(seconds)
            text_content = str(self.max_time - self.time)
            ui.run(text_content, str(player.life))

            pygame.display.flip()
            FPSclock.tick(30)
