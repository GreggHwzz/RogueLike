import pygame, sys
import constants
from button import Button
from character import Character

pygame.init()

ecran_info = pygame.display.Info()
largeur = ecran_info.current_w
hauteur = ecran_info.current_h

SCREEN = pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

MUSIC = pygame.mixer.music.load('music/main_theme.mp3')
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)

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
        
        EXIT_BUTTON = Button(image=None, pos=(100,40), text_input="Quitter", font=get_font(20), base_color="Grey", hovering_color="White")
        BACK_BUTTON = Button(image=None, pos=(300,40), text_input="Retour", font=get_font(20), base_color="Grey", hovering_color="White")
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
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
        player.draw(SCREEN,0)
    
        for button in [EXIT_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
            
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

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(100).render("OPTIONS", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN.get_width()//2, 190))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(SCREEN.get_width()//2, 700), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        
        MUSIC_OFF = Button(image=None, pos=(600,460), 
                            text_input="MUSIC OFF", font=get_font(75), base_color="Brown", hovering_color="RED")
        
        MUSIC_ON = Button(image=None, pos=(SCREEN.get_width()-600, 460), 
                            text_input="MUSIC ON", font=get_font(75), base_color="#007113", hovering_color="#00D123")
        
        for button in [OPTIONS_BACK,MUSIC_ON,MUSIC_OFF]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if MUSIC_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.pause()
                if MUSIC_ON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.unpause()
                        
        pygame.display.update()
        
    
def main_menu():
    while True:
        SCREEN.fill((1,0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Efreyan Adventures", True, "#057DC1")
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
    