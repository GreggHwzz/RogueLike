
from items import Item
import constants
from player import Player
from enemy import Enemy

class World():
  def __init__(self):
    self.map_tiles = []
    self.obstacle_tiles = []
    self.exit_tile = None
    self.item_list = []
    self.player = None
    self.character_list = []
    self.enemy = None


  def process_data(self, data, tile_list, item_images):
    self.level_length = len(data)
    #iterate through each value in level data file
    for y, row in enumerate(data):
      for x, tile in enumerate(row):
        image = tile_list[tile]
        image_rect = image.get_rect()
        image_x = x * constants.TILE_SIZE
        image_y = y * constants.TILE_SIZE
        image_rect.center = (image_x, image_y)
        tile_data = [image, image_rect, image_x, image_y]

        #add image data to main tiles list
        if tile >= 0:
          self.map_tiles.append(tile_data)
        elif tile == 7:
          self.obstacle_tiles.append(tile_data)
        elif tile == 8:
          self.exit_tile = tile_data
        elif tile == 9:
          coin = Item(image_x, image_y, 0, "assets/coin_f0.png")
          self.item_list.append(coin)
          tile_data[0] = tile_list[0]
        elif tile == 10:
          potion = Item(image_x, image_y, 1, "assets/potion.png")
          self.item_list.append(potion)
          tile_data[0] = tile_list[0]
        elif tile == 11:
          player = Player(image_x, image_y, 100, 1)
          self.character_list.append(player)
          tile_data[0] = tile_list[0]
        elif tile >= 12 and tile <= 17:
          enemy = Enemy(image_x, image_y, 100, 1,"assets/skeleton/skeleton.png")
          self.enemy=enemy
          self.character_list.append(enemy)
          tile_data[0] = tile_list[0]
          
        #add image data to main tiles list
        if tile >= 0:
          self.map_tiles.append(tile_data)

  def update(self, screen_scroll):
    for tile in self.map_tiles:
      tile[2] += screen_scroll[0]
      tile[3] += screen_scroll[1]
      tile[1].center = (tile[2], tile[3])

  def draw(self, surface):
    for tile in self.map_tiles:
      surface.blit(tile[0], tile[1])