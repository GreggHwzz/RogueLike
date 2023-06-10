import pygame, sys
import constants
from button import Button
from character import Character

pygame.init()

SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

clock = pygame.time.Clock()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    clock = pygame.time.Clock()
    #Definition des variables de mouvements
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    #Création de personnage
    player = Character(100,100)
    while True:
        clock.tick(constants.FPS)
    
        SCREEN.fill(constants.BG)
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
        player.draw(SCREEN)
    
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
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.fill((1,0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Efreyan Adventures", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN.get_width()//2,200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)-100)), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)+150)), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(SCREEN.get_width()//2,((SCREEN.get_height()//2)+400)), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
    