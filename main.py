import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Roguelike Project")

clock = pygame.time.Clock()

#Definition des variables de mouvements
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#Création de personnage
player = Character(100,100)

#main game loop
run = True
while run:
    
    clock.tick(constants.FPS)
    
    screen.fill(constants.BG)
    #Calcul des mouvements du joueur
    dx = 0
    dy = 0
    if moving_left == True:
        dx = -constants.SPEED
    if moving_right == True:
        dx = constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED
    
    #Mouvement du personnage 
    player.move(dx,dy)
    
    #Affichage du personnage sur l'écran
    player.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                moving_up = True
            if event.key == pygame.K_q:
                moving_left = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_d:
                moving_right = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                moving_up = False
            if event.key == pygame.K_q:
                moving_left = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_d:
                moving_right = False
                
    pygame.display.update()

pygame.quit()