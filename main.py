import json
import pygame, sys
import pygame.sprite
import constants
from button import Button
from character import Character
from healthbar import HealthBar


from bullet import Bullet
from enemy import Enemy
from items import Item
from player import Player
from dungeonn import Dungeon
from sprites import Floor
pygame.init()

ecran_info = pygame.display.Info()
largeur = ecran_info.current_w
hauteur = ecran_info.current_h

bullet_group=pygame.sprite.Group()

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
    shoot=False

    

    with open('maps.json') as f:
        data = json.load(f)
        m = 0
        for map in data:
            constants.MAPS.append([])
            n = 0
            for j in range(constants.TILESIZE):
                constants.MAPS[m].append([])
                for i in range(constants.TILESIZE):
                    constants.MAPS[m][j].append(data.get(str(map))[n])
                    n += 1
            m += 1

    donjoonn = Dungeon()
    donjoonn.new(5)
    


    #Création de personnage
    player=donjoonn.getPlayer()
    en1= Enemy(SCREEN.get_width()-20,SCREEN.get_height()-20,100)
    en2= Enemy(SCREEN.get_width()-100,SCREEN.get_height()-20,100)
    
    #Création d'items
    health_potion= Item(SCREEN.get_width()-100,100, "health", "assets/potion.png")
    



    
   
    
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
        if shoot == True:
            
            player.shoot()
        

    
        #Mouvement du personnage 
        player.move(dx,dy)
        for enemy in Enemy.enemies_group:
            if enemy!=None:
                enemy.move(player)

        #Mort enemies
        for enemy in Enemy.enemies_group:
            if enemy!=None:
                if enemy.hp<=0:
                    Enemy.enemies_group.remove(enemy)
                    del enemy
                    enemy=None
    
        #Affichage du personnage sur l'écran
        donjoonn.draw(SCREEN)
        player.draw(SCREEN)
        player.update()
        for enemy in Enemy.enemies_group:
            if enemy!=None:
                enemy.draw(SCREEN)
        player.bullets.update()
        player.bullets.draw(SCREEN)

        if player.healthbar.hp <= 0:
            GAME_OVER_TEXT = get_font(100).render("Game Over", True, constants.RED)
            GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(SCREEN.get_width() // 2, 700))
            SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)
            SCREEN.blit(pygame.transform.scale(pygame.image.load('assets/dinosaure/doux15.png'),(40,40)), player.rect)

        #Affichage de la barre de vie
        player.healthbar.draw(SCREEN)

        #Affichage des items 
        if (health_potion != None):
                if(health_potion.effect(player)): 
                    del health_potion
                    health_potion = None
                else:  health_potion.draw(SCREEN)
            
       
    
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
                    player.is_moving=True
                if event.key == pygame.K_q:
                    moving_left = True
                    player.is_moving=True
                if event.key == pygame.K_s:
                    moving_down = True
                    player.is_moving=True
                if event.key == pygame.K_d:
                    moving_right = True
                    player.is_moving=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                shoot = True
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    moving_up = False
                    player.is_moving=False
                if event.key == pygame.K_q:
                    moving_left = False
                    player.is_moving=False
                if event.key == pygame.K_s:
                    moving_down = False
                    player.is_moving=False
                if event.key == pygame.K_d:
                    moving_right = False
                    player.is_moving=False
            if event.type == pygame.MOUSEBUTTONUP:
                shoot = False
                
        pygame.display.flip()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(100).render("OPTIONS", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN.get_width()//2, 190))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(SCREEN.get_width()//2, 700), 
                            text_input="RETOUR", font=get_font(75), base_color="White", hovering_color="Green")
        
        MUSIC_OFF = Button(image=None, pos=(400,460), 
                            text_input="MUSIC OFF", font=get_font(75), base_color="Brown", hovering_color="RED")
        
        MUSIC_ON = Button(image=None, pos=(SCREEN.get_width()-360, 460), 
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
    def update_text():
        global font
        font = pygame.font.Font("assets/font.ttf", 90)
        text_color = "#057DC1"
        text = "RogueLike Prototype"
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect()

        # Positionnez le texte au centre de l'écran
        text_rect.center = (SCREEN.get_width() // 2, 200)

        # Redimensionnez le texte en fonction de la taille de l'écran
        if text_rect.width > SCREEN.get_width() or text_rect.height > SCREEN.get_height():
            new_font_size = int(font.size(text)[1] * min(SCREEN.get_width() / text_rect.width, SCREEN.get_height() / text_rect.height))
            font = pygame.font.Font("assets/font.ttf", new_font_size)
            text_surface = font.render(text, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.center = (SCREEN.get_width() // 2, 200)

        return text_surface, text_rect
    while True:
        SCREEN.fill((1,0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)-70)), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)+100)), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(SCREEN.get_width()//2,((SCREEN.get_height()//2)+290)), 
                            text_input="QUITTER", font=get_font(75), base_color="#d7fcd4", hovering_color="Red")

        text_surface, text_rect = update_text()
        
        SCREEN.blit(text_surface, text_rect)

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
    