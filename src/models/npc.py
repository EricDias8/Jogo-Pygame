import pygame, random
from src.models.entity import Entity
from src.settings import *

class Npc(Entity):
    def __init__(self, sprite, x, y, speed, width, height, scale):
        super().__init__(sprite, x, y, speed, width, height, scale, "")
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.colisao = False
        self.lastX = 0
        self.lastY = 0
        self.interval = 0
        self.target_x = x
        self.target_y = y
        self.speed = 0
        self.max_speed = 3
        self.acceleration = 0.1
        self.state = 0
        self.anim_steps = [3, 3, 3, 3]
        self.anim = []
        self.last_update = pygame.time.get_ticks()
        self.frame_tick = 120
        self.cur_frame = 0
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
        if (self.x == self.target_x and self.y == self.target_y):
            self.target_x = random.randint(0, WIDTH)
            self.target_y = random.randint(0, HEIGHT)

        direction_x = self.target_x - self.x
        direction_y = self.target_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5

        if self.speed < self.max_speed:
            self.speed += self.acceleration

        self.speed = min(self.speed, distance)

        if(self.colisao == False):
            self.lastX = self.x
            self.lastY = self.y
            if distance > 0:
                self.x += direction_x * (self.speed / distance)
                self.y += direction_y * (self.speed / distance)

            if(direction_x * (self.speed / distance) > 0):
                self.right = True
                self.left = False
            else:
                self.left = True
                self.right = False
            
            if(direction_y * (self.speed / distance) > 0):
                if(abs(direction_x * (self.speed / distance)) < abs(direction_y * (self.speed / distance))):
                    self.left = False
                    self.right = False
                    self.up = False
                    self.down = True
            else:
                if(abs(direction_x * (self.speed / distance)) < abs(direction_y * (self.speed / distance))):
                    self.left = False
                    self.right = False
                    self.up = True
                    self.down = False
            
        
        if(self.up or self.down or self.left or self.right):
            if(self.up):
                self.state = 3
            elif(self.down):
                self.state = 0
            if(self.left):
                self.state = 1
            elif(self.right):
                self.state = 2
        else:
            self.state = 0

    def Draw(self, screen):
        cur_time = pygame.time.get_ticks()
        if cur_time - self.last_update >= self.frame_tick:
            self.cur_frame += 1
            self.last_update = cur_time
            if self.cur_frame == len(self.anim[self.state]):
                self.cur_frame = 0
        screen.blit(self.anim[self.state][self.cur_frame], (self.x, self.y))

    def block(self):
        if(self.colisao):
            self.x = self.lastX
            self.y = self.lastY
            self.target_x = random.randint(0, WIDTH)
            self.target_y = random.randint(0, HEIGHT)
            self.colisao = False
    
    def DrawHitbox(self, screen):
        pygame.draw.rect(screen, (255,255,0), (self.x+20, self.y+40, self.width-20, self.height/2),4)

    def isColliding(self, entity2):
        other_rect = pygame.Rect(entity2.x, entity2.y, entity2.width * entity2.scale, entity2.height * entity2.scale)
        my_rect = pygame.Rect(self.x+20, self.y+40, self.width-20, self.height/2)
        if(my_rect.colliderect(other_rect)):
            return True
        return False

        
