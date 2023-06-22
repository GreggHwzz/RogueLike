import pygame
import pygame.sprite
import math
import constants
from bullet import Bullet
from healthbar import HealthBar

class Character():
    def __init__(self,x,y, max_hp):
         self.rect = pygame.Rect(0,0,70,70)
         self.rect.center = (x,y)
         self.image = pygame.image.load("assets/doux.png").convert_alpha()
         self.direction=1
         self.hp = max_hp
         self.max_hp = max_hp
         self.healthbar=HealthBar(50,850,200,20,self.max_hp)
         
         
    
      
        
    