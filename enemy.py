import pygame
import pygame.sprite
from  pygame.sprite import Group

import math
import constants
from character import Character

class Enemy(Character):
    walkLeft = [pygame.image.load('assets/skeleton/skeleton.png'), pygame.image.load('assets/skeleton/skeleton1.png'), pygame.image.load('assets/skeleton/skeleton2.png'), pygame.image.load('assets/skeleton/skeleton3.png'), pygame.image.load('assets/skeleton/skeleton4.png'), pygame.image.load('assets/skeleton/skeleton5.png'), pygame.image.load('assets/skeleton/skeleton6.png'), pygame.image.load('assets/skeleton/skeleton7.png')]
    walkRight = [pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton.png'), True, False), pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton1.png'), True, False), pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton2.png'), True, False), pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton3.png'), True, False), pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton4.png'), True, False), pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton5.png'), True, False), pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton6.png'), True, False),pygame.transform.flip(pygame.image.load('assets/skeleton/skeleton7.png'), True, False)]
    enemies_group = pygame.sprite.Group()
    def __init__(self, x, y,  max_hp,size,image):
        super().__init__(x,y, max_hp, size, image)
        self.animation_speed = 0.2
        self.animation_timer = 0
        self.walkCount = 0
        self.is_moving = False
        self.hp = max_hp
    
    def draw(self, surface):
        if self.is_moving:
            self.animation_timer += self.animation_speed  # Gestion de la vitesse de l'animation
            if self.animation_timer >= 1:
                self.walkCount += 1
                self.animation_timer = 0

                if self.walkCount >= 8:
                    self.walkCount = 0
            if self.direction > 0: 
                surface.blit(self.walkRight[self.walkCount], self.rect)
            else:  
                surface.blit(self.walkLeft[self.walkCount], self.rect)
        else:
            surface.blit(self.walkLeft[0], self.rect)
        
            
    def damages(self, player):
        
        player.healthbar.hp-=1
        
    def move(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery- self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance <=20:
            self.damages(player)
            self.is_moving = False
            
        else:
            dx /= distance
            dy /= distance
            self.is_moving = True

            self.rect.x += dx    # Vitesse de déplacement de l'ennemi
            self.rect.y += dy   # Vitesse de déplacement de l'ennemi
        if dx > 0:
            self.direction = 1
        elif dx < 0:
            self.direction =-1

       
    

