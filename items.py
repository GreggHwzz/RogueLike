import pygame
import pygame.sprite
import math
import constants
from healthbar import HealthBar


class Item():
    def __init__(self,x,y,type,image):
        self.rect = pygame.Rect(0,0,50,50)
        self.rect.center = (x,y)
        self.type=type    
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(50,35))

    def effect(self,player):
        if (type=="health"):
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery- self.rect.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)
            print(self.rect.centerx, self.rect.centery)
            if distance<=2:
                print("fck")
                player.healthbar.hp-=10
    
    def draw(self,surface):
        
        surface.blit(self.image, self.rect)
