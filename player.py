import pygame
import pygame.sprite
import math
import constants
from bullet import Bullet
from healthbar import HealthBar
from character import Character

class Player(Character):
    walkRight = [pygame.image.load('assets/dinosaure/doux.png'), pygame.image.load('assets/dinosaure/doux2.png'), pygame.image.load('assets/dinosaure/doux3.png'), pygame.image.load('assets/dinosaure/doux4.png'), pygame.image.load('assets/dinosaure/doux5.png'), pygame.image.load('assets/dinosaure/doux6.png'), pygame.image.load('assets/dinosaure/doux7.png'), pygame.image.load('assets/dinosaure/doux8.png'),pygame.image.load('assets/dinosaure/doux9.png'), pygame.image.load('assets/dinosaure/doux10.png'), pygame.image.load('assets/dinosaure/doux11.png'), pygame.image.load('assets/dinosaure/doux12.png'), pygame.image.load('assets/dinosaure/doux13.png')]
    walkLeft = [pygame.transform.flip(pygame.image.load('assets/dinosaure/doux.png'), True, False), pygame.transform.flip(pygame.image.load('assets/dinosaure/doux2.png'), True, False), pygame.transform.flip(pygame.image.load('assets/dinosaure/doux3.png'), True, False), pygame.transform.flip(pygame.image.load('assets/dinosaure/doux4.png'), True, False), pygame.transform.flip(pygame.image.load('assets/dinosaure/doux5.png'), True, False), pygame.transform.flip(pygame.image.load('assets/dinosaure/doux6.png'), True, False), pygame.transform.flip(pygame.image.load('assets/dinosaure/doux7.png'), True, False),pygame.transform.flip(pygame.image.load('assets/dinosaure/doux8.png'), True, False),pygame.transform.flip(pygame.image.load('assets/dinosaure/doux9.png'), True, False),pygame.transform.flip(pygame.image.load('assets/dinosaure/doux10.png'), True, False),pygame.transform.flip(pygame.image.load('assets/dinosaure/doux11.png'), True, False),pygame.transform.flip(pygame.image.load('assets/dinosaure/doux12.png'), True, False),pygame.transform.flip(pygame.image.load('assets/dinosaure/doux13.png'), True, False)]
    def __init__(self,x,y, max_hp,size):
        super().__init__(x,y,max_hp,size)
        self.image = pygame.image.load("assets/doux.png").convert_alpha()
        self.shoot_cooldown=0
        self.bullets=pygame.sprite.Group()
        self.animation_speed = 0.2
        self.animation_timer = 0
        self.walkCount = 0
        self.is_moving = False
        self.healthbar=HealthBar(50,pygame.display.get_surface().get_height()-80,200,20,max_hp)
        self.direction=1

    def draw(self, surface):
        if self.is_moving:
            self.animation_timer += self.animation_speed  # Gestion de la vitesse de l'animation
            if self.animation_timer >= 1:
                self.walkCount += 1
                self.animation_timer = 0

                if self.walkCount >= 8:
                    self.walkCount = 0
            if self.direction > 0: 
                surface.blit(pygame.transform.scale(self.walkRight[self.walkCount],(40,40)), self.rect)
            else:  
                surface.blit(pygame.transform.scale(self.walkLeft[self.walkCount],(40,40)), self.rect)
        else:
            surface.blit(pygame.transform.scale(self.walkLeft[0],(40,40)), self.rect)

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction_x = mouse_x - self.rect.centerx
            direction_y = mouse_y - self.rect.centery
            distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
            if distance > 0:
                direction_x /= distance
                direction_y /= distance
            bullet = Bullet(self.rect.centerx -10, self.rect.centery, (direction_x, direction_y))
            self.bullets.add(bullet)
            
    def update(self):
        if self.shoot_cooldown>0:
            self.shoot_cooldown-=1
