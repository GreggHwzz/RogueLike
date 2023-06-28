import pygame
import pygame.sprite
import constants
from enemy import Enemy

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 10
        self.image = pygame.transform.scale(pygame.image.load("assets/boulebleue.png").convert_alpha(), (13, 13))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.rect.x += self.direction[0] * self.speed  # Met à jour la position horizontale de la balle
        self.rect.y += self.direction[1] * self.speed  # Met à jour la position verticale de la balle

        if self.rect.right < 0 or self.rect.left > pygame.display.Info().current_w:
            self.kill()  # Détruit la balle si elle quitte l'écran
        self.damages()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def damages(self):
        enemy_hit_list = pygame.sprite.spritecollide(self, Enemy.enemies_group, False)
        for enemy in enemy_hit_list:
            enemy.hp -= 20     
            self.kill()

    