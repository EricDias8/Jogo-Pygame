import pygame
from src.models.entity import Entity

class Player(Entity):
    life = 3
    directions = ["left", "down", "right", "up"]
    actualDirection = directions[0]
    colisao = False
    walkSpriteFrame = [1, 3] #ESQUERDA DIREITA
    currentFrame = walkSpriteFrame[0]
    up = False
    down = False
    left = False
    right = False
    state = 0
    lastX = 0
    lastY = 0
    frontPosition = (0,0)
    anim = []
    anim_steps = [9, 4, 9, 4]
    last_update = pygame.time.get_ticks()
    frame_tick = 120
    cur_frame = 0
    height = 0
    width = 0
    time = 0
    def __init__(self, sprite, x, y, speed, width, height, scale):
        super().__init__(sprite, x, y, speed, width, height, scale, "")
        j = 0
        for animation in self.anim_steps:
            temp_list = []
            i = 0
            for _ in range(animation):
                temp_list.append(sprite.get_image(i, j, self.width, self.height, self.scale, (255,255,255)))
                i += 1
            j += 1
            self.anim.append(temp_list)

    def Move(self):
        if(self.colisao == False):
            self.lastX = self.x
            self.lastY = self.y
            if(self.up or self.down or self.left or self.right):
                self.state = self.currentFrame
                if(self.up):
                    self.actualDirection = self.directions[3]
                    self.y -= self.speed
                elif(self.down):
                    self.actualDirection = self.directions[1]
                    self.y += self.speed
                if(self.left):
                    self.actualDirection = self.directions[0]
                    self.x -= self.speed
                elif(self.right):
                    self.actualDirection = self.directions[2]
                    self.x += self.speed
            else:
                if(self.currentFrame == self.walkSpriteFrame[0]):
                    self.state = 0
                else:
                    self.state = 2

    def Draw(self, screen):
        cur_time = pygame.time.get_ticks()
        if cur_time - self.last_update >= self.frame_tick:
            self.cur_frame += 1
            self.last_update = cur_time
            if self.cur_frame == len(self.anim[self.state]):
                self.cur_frame = 0
        screen.blit(self.anim[self.state][self.cur_frame], (self.x, self.y))
        #pygame.draw.rect(screen, (255,0,255), (self.x+20, self.y+50, self.width/5, self.height/5), 3)

    def block(self):
            if(self.colisao):
                self.x = self.lastX
                self.y = self.lastY
                self.colisao = False

    def getPlayerFront(self, screen):
        '''
        if self.actualDirection == "left":
            pygame.draw.rect(screen, (255,255,0), (self.x-40, self.y+60, 20 , 20) ,4)
            pos = [self.x-40, self.y+60]
        if self.actualDirection == "right":
            pygame.draw.rect(screen, (255,255,0), (self.x+130, self.y+60, 20 , 20) ,4)
            pos = [self.x+130, self.y+60]
        if self.actualDirection == "up":
            pygame.draw.rect(screen, (255,255,0), (self.x+45, self.y-50, 20 , 20) ,4)
            pos = [self.x+45, self.y-50]
        if self.actualDirection == "down":
            pygame.draw.rect(screen, (255,255,0), (self.x+45, self.y+150, 20 , 20) ,4)
            pos = [self.x+45, self.y+150]
        '''
        pos = [self.x, self.y]
        return pos