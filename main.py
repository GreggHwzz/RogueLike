import pygame
import sys
import csv
from world import World
from button import Button
from items import Item
import constants

pygame.init()

ecran_info = pygame.display.Info()
largeur = ecran_info.current_w
hauteur = ecran_info.current_h

SCREEN = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("RogueLike Prototype")

MUSIC = pygame.mixer.music.load('music/main_theme.mp3')
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()



def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    clock = pygame.time.Clock()
    #Definition des variables de mouvements
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    shoot = False
    
    #define game variables
    level = 1
    screen_scroll = [0, 0]

#load tilemap images
    tile_list = []
    for x in range(constants.TILE_TYPES):
        tile_image = pygame.image.load(f"assets/tiles/{x}.png").convert_alpha()
        tile_image = pygame.transform.scale(tile_image, (constants.TILE_SIZE, constants.TILE_SIZE))
        tile_list.append(tile_image)

#helper function to scale image
    def scale_img(image, scale):
        w = image.get_width()
        h = image.get_height()
        return pygame.transform.scale(image, (w * scale, h * scale))

#load coin images
    coin_images = []
    for x in range(4):
        img = scale_img(pygame.image.load("assets/coin_f0.png").convert_alpha(), constants.ITEM_SCALE)
        coin_images.append(img)

    item_images = []
    item_images.append(coin_images)

#function to reset level
    def reset_level():
    #create empty tile list
        data = []
        for row in range(constants.ROWS):
           r = [-1] * constants.COLS
           data.append(r)

        return data

#create empty tile list
    world_data = []
    for row in range(constants.ROWS):
        r = [-1] * constants.COLS
        world_data.append(r)

#load in level data and create world
    with open(f"levels/level{level}_data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        for x, row in enumerate(reader):
            for y, tile in enumerate(row):
                world_data[x][y] = int(tile)

    world = World()
    world.process_data(world_data, tile_list, item_images)
#Création de personnage
    player = world.player
    en1= world.enemy
    #Création d'items
    health_potion = Item(SCREEN.get_width()-100, 100, "health", "assets/potion.png")

    while True:
        clock.tick(constants.FPS)

        SCREEN.fill(constants.BG)

        EXIT_BUTTON = Button(image=None, pos=(100, 40), text_input="Quitter", font=get_font(20), base_color="Grey", hovering_color="White")
        BACK_BUTTON = Button(image=None, pos=(300, 40), text_input="Retour", font=get_font(20), base_color="Grey", hovering_color="White")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #Calcul des mouvements du player
        dx = 0
        dy = 0

        if moving_left:
            dx = -constants.SPEED
        if moving_right:
            dx = constants.SPEED
        if moving_up:
            dy = -constants.SPEED
        if moving_down:
            dy = constants.SPEED
        if shoot:
            player.shoot()

        #Mouvement du personnage
        player.update()
        player.draw(SCREEN)
        
        player.bullets.update()
        player.bullets.draw(SCREEN)

        #Affichage de la barre de vie
        player.healthbar.draw(SCREEN)

        #Affichage des items
        if health_potion is not None:
            if health_potion.effect(player):
                health_potion = None
            else:
                health_potion.draw(SCREEN)

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
                    player.is_moving = True
                if event.key == pygame.K_q:
                    moving_left = True
                    player.is_moving = True
                if event.key == pygame.K_s:
                    moving_down = True
                    player.is_moving = True
                if event.key == pygame.K_d:
                    moving_right = True
                    player.is_moving = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    moving_up = False
                    player.is_moving = False
                if event.key == pygame.K_q:
                    moving_left = False
                    player.is_moving = False
                if event.key == pygame.K_s:
                    moving_down = False
                    player.is_moving = False
                if event.key == pygame.K_d:
                    moving_right = False
                    player.is_moving = False

            if event.type == pygame.MOUSEBUTTONUP:
                shoot = False

        level_complete = player.move(dx, dy, world.obstacle_tiles, world.exit_tile)

        if level_complete:
            start_intro = True
            level += 1
            world_data = reset_level()
            #load in level data and create world
            with open(f"levels/level{level}_data.csv", newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        world_data[x][y] = int(tile)
            world = World()
            world.process_data(world_data, tile_list, item_images)
            temp_hp = player.health
            temp_score = player.score
            player = world.player
            player.health = temp_hp
            player.score = temp_score

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

        MUSIC_OFF = Button(image=None, pos=(600, 460),
                            text_input="MUSIC OFF", font=get_font(75), base_color="Brown", hovering_color="RED")

        MUSIC_ON = Button(image=None, pos=(SCREEN.get_width()-600, 460),
                            text_input="MUSIC ON", font=get_font(75), base_color="#007113", hovering_color="#00D123")

        for button in [OPTIONS_BACK, MUSIC_ON, MUSIC_OFF]:
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
        SCREEN.fill((1, 0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)-100)),
                            text_input="COMMENCER", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)+150)),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(SCREEN.get_width()//2, ((SCREEN.get_height()//2)+400)),
                            text_input="QUITTER", font=get_font(75), base_color="#d7fcd4", hovering_color="Red")

        text_surface, text_rect = update_text()

        # Affiche le texte sur l'écran
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
