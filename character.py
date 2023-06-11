import pygame
import pygame.sprite
import math
import constants
from bullet import Bullet

class Character():
    def __init__(self,x,y):
         self.rect = pygame.Rect(0,0,70,70)
         self.rect.center = (x,y)
         self.image = pygame.image.load("assets/doux.png").convert_alpha()
         self.pistolet = pygame.transform.scale(pygame.image.load("assets/pistolet.png").convert_alpha(), (23, 15)) 
         self.direction=1
         self.shoot_cooldown=0
         self.bullets=pygame.sprite.Group()
         
         
    def draw(self,surface, frame):
        surface.blit(self.image, self.rect, pygame.Rect(48*frame, 0, 48, 48))
        self.image.set_colorkey((0,0,0))
        self.rect = pygame.Rect(0, 0, 48, 48)
        self.rect.center=(x,y)
        self.image = pygame.image.load("doux.png").convert_alpha()
      
        
    def draw(self,surface,frame):
        if self.direction==1:

            surface.blit(self.image, self.rect, pygame.Rect(48*frame, 0, 48, 48))
            self.image.set_colorkey((0,0,0))
        
            surface.blit(self.pistolet, (self.rect.x + 30, self.rect.y + 20))
        
        elif self.direction==-1:
            flipped_image = pygame.transform.flip(self.image, True, False)
            surface.blit(flipped_image, self.rect, pygame.Rect(self.image.get_width()-(48 +48*frame), 0, 48, 48))
            flipped_gun= pygame.transform.flip(self.pistolet, True, False)
            surface.blit(flipped_gun, (self.rect.x - 5, self.rect.y + 20))

    def move(self,dx,dy):
        
        if dx != 0 and dy != 0:
            dx *= math.sqrt(2)/2
            dy *= math.sqrt(2)/2
            
        self.rect.x += dx
        self.rect.y += dy

        if dx>0:
            self.direction=1
        elif dx<0:
            self.direction =-1

    def shoot(self):
        if self.shoot_cooldown==0:
            self.shoot_cooldown=20
            bullet=None
            if self.direction==1:
                bullet=Bullet(self.rect.centerx + (self.rect.size[0]*0.3 ), self.rect.centery - 13, self.direction)
                
            if self.direction==-1:
                bullet=Bullet(self.rect.centerx - (self.rect.size[0]*0.6 ), self.rect.centery - 13, self.direction)
            if bullet is not None:  # Vérification si bullet a été défini
                self.bullets.add(bullet)
        

    def update(self):
        if self.shoot_cooldown>0:
            self.shoot_cooldown-=1