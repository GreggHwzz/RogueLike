import pygame
import math
import constants

class Character():
    def __init__(self,x,y):
         self.rect = pygame.Rect(0,0,40,40)
         self.rect.center = (x,y)
         
    def draw(self,surface):
        pygame.draw.rect(surface, constants.RED, self.rect)
    
    def move(self,dx,dy):
        
        if dx != 0 and dy != 0:
            dx *= math.sqrt(2)/2
            dy *= math.sqrt(2)/2
            
        self.rect.x += dx
        self.rect.y += dy