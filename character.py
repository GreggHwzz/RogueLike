import pygame
import pygame.sprite
import math
import constants

from healthbar import HealthBar

class Character(pygame.sprite.Sprite):
    def __init__(self,x,y):
         pygame.sprite.Sprite.__init__(self)
         self.rect = pygame.Rect(0,0,70,70)
         self.rect.center = (x,y)
         
         self.direction=1
         
         
         
         
    
      
        
    