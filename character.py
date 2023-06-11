import pygame
import math
import constants

class Character():
    def __init__(self,x,y):
         self.rect = pygame.Rect(0,0,70,70)
         self.rect.center = (x,y)
         self.image = pygame.image.load("assets/doux.png").convert_alpha()
         
    def draw(self,surface, frame):
        surface.blit(self.image, self.rect, pygame.Rect(48*frame, 0, 48, 48))
        self.image.set_colorkey((0,0,0))
    
    def move(self,dx,dy):
        
        if dx != 0 and dy != 0:
            dx *= math.sqrt(2)/2
            dy *= math.sqrt(2)/2
            
        self.rect.x += dx
        self.rect.y += dy