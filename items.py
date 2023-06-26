import pygame
import pygame.sprite
import math
import constants


class Item():
    def __init__(self,x,y,type,image):
        self.rect = pygame.Rect(0,0,50,50)
        self.rect.center = (x,y)
        self.type=type    
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(50,35))
 
    def effect(self,player):
        if (self.type=="health"):
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery- self.rect.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance<=20: 
                player.healthbar.add_hp(30)         
                return True
        return False 
    
    def draw(self,surface):
        
        surface.blit(self.image, self.rect)
