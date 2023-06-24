import pygame
import constants

DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
class Wall(pygame.sprite.Sprite):
    walls=pygame.sprite.Group()

    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((constants.TILESIZE, constants.TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * constants.TILESIZE
        self.rect.y = y * constants.TILESIZE
        Wall.walls.add(self)

class Floor(pygame.sprite.Sprite):
    floors=pygame.sprite.Group()

    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((constants.TILESIZE, constants.TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * constants.TILESIZE
        self.rect.y = y * constants.TILESIZE
        Floor.floors.add(self)