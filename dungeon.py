import pygame
import random
import constants

class Tilemap:
    def __init__(self, x, y):
        self.tiles = [[0] * (constants.ROOM_SIZE // constants.WALL_SIZE) for _ in range(constants.ROOM_SIZE // constants.WALL_SIZE)]
        self.x = x
        self.y = y
        self.generate()

    def generate(self):
        # Add walls
        for i in range(len(self.tiles)):
            self.tiles[0][i] = 1
            self.tiles[-1][i] = 1
            self.tiles[i][0] = 1
            self.tiles[i][-1] = 1

        # Add doors
        doors = random.sample([(0, constants.ROOM_SIZE // 2), (constants.ROOM_SIZE // 2, 0), (constants.ROOM_SIZE - 1, constants.ROOM_SIZE // 2), (constants.ROOM_SIZE // 2, constants.ROOM_SIZE - 1)], 2)
        for door in doors:
            self.tiles[door[1] // constants.WALL_SIZE][door[0] // constants.WALL_SIZE] = 0

    def draw(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                if self.tiles[y][x] == 1:
                    pygame.draw.rect(pygame.display.set_mode((0, 0), pygame.FULLSCREEN), constants.BLACK, (self.x + x * constants.WALL_SIZE, self.y + y * constants.WALL_SIZE, constants.WALL_SIZE, constants.WALL_SIZE))
                elif self.tiles[y][x] == 0:
                    pygame.draw.rect(pygame.display.set_mode((0, 0), pygame.FULLSCREEN), constants.WHITE, (self.x + x * constants.WALL_SIZE, self.y + y * constants.WALL_SIZE, constants.WALL_SIZE, constants.WALL_SIZE))
