import pygame, sys, math, random, copy
from sprites import Wall, Floor

from player import Player

import constants

class Dungeon(object):
    

    def __init__(self):
        self.dungeon = []
        
       
        

    def new(self, dungeonSize):
        self.dungeonSize = dungeonSize
        self.createDungeon()
        self.addAdjacent()
        self.fillWall()
        self.createDungeonObject()
        self.newPlayer()
        
       

    def getDungeon(self):
        return self.dungeon

    def getPlayer(self):
        return self.player

    # Create the dungeon

    def createDungeon(self):
        self.dungeon.clear()
        self.adjacent = []
        self.adjacent.append(((self.dungeonSize) // 2, (self.dungeonSize) // 2))
        for j in range(self.dungeonSize):
            self.dungeon.append([])
            for i in range(self.dungeonSize):
                self.dungeon[j].append([])

    def addAdjacent(self):
        dungeonSizeItr = self.dungeonSize
        while dungeonSizeItr >= 0:
            index = random.randint(0, len(self.adjacent)-1)
            point = self.adjacent[index]
            del self.adjacent[index]
            if point[0] -1 >= 0 and not self.dungeon[point[0] -1][point[1]]:
                self.adjacent.append((point[0] -1, point[1]))
            if point[0] +1 < self.dungeonSize and not self.dungeon[point[0] +1][point[1]]:
                self.adjacent.append((point[0] +1, point[1]))
            if point[1] -1 >= 0 and not self.dungeon[point[0]][point[1] -1]:
                self.adjacent.append((point[0], point[1] -1))
            if point[1] +1 < self.dungeonSize and not self.dungeon[point[0]][point[1] +1]:
                self.adjacent.append((point[0], point[1] +1))
            self.dungeon[point[0]][point[1]].append(copy.deepcopy(random.choice(constants.MAPS)))
            dungeonSizeItr -= 1

    def fillWall(self):
        
        for j in range(self.dungeonSize):
            for i in range(self.dungeonSize):
                if self.dungeon[j][i]:
                    dungeon = self.dungeon[j][i][0]
                    if j -1 < 0 or not self.dungeon[j - 1][i]: #top
                        for n in range(6, 10):
                            dungeon[0][n].remove(0)
                            dungeon[0][n].append(2)
                    if j +1 >= self.dungeonSize or not self.dungeon[j + 1][i]: #down
                        for n in range(6, 10):
                            
             

                                dungeon[constants.TILESIZE -1][n].remove(0)
                                dungeon[constants.TILESIZE -1][n].append(2)
                    if i -1 < 0 or not self.dungeon[j][i - 1]: #left
                        for n in range(6, 10):
                            dungeon[n][0].remove(0)
                            dungeon[n][0].append(2)
                    if i +1 >= self.dungeonSize or not self.dungeon[j][i + 1]: #right
                        for n in range(6, 10):
                            
                                dungeon[n][constants.TILESIZE -1].remove(0)
                                dungeon[n][constants.TILESIZE -1].append(2)

    
    def createDungeonObject(self):

        offseti, offsetj = 0, 0
        for jd in range(self.dungeonSize):
            for id in range(self.dungeonSize):
                dungeon = self.dungeon[jd][id]
                if dungeon:
                    dungeon = dungeon[0]
                    
                    for j in range(len(dungeon)):
                        for i in range(len(dungeon[j])):

                            tmp = []
                            for case in dungeon[j][i]:
                                if case == 1 or case == 2:
                                    tmp.append(Wall(i + offseti, j + offsetj))
                                    
                                elif case == 0:
                                    tmp.append(Floor( i + offseti, j + offsetj))
                                
                            dungeon[j][i].clear()
                            dungeon[j][i] = tmp
                offseti += constants.TILESIZE
            offsetj += constants.TILESIZE
            offseti = 0
            

    def draw(self,SCREEN):
        for sprite in Floor.floors:
            SCREEN.blit(sprite.image,  sprite.rect)
        for sprite in Wall.walls:
            
            SCREEN.blit(sprite.image,  sprite.rect)

    def newPlayer(self):
        print (Wall.walls)
        dungeon = self.dungeon[self.dungeonSize // 2][self.dungeonSize // 2][0]
        for j in range(constants.TILESIZE):
            for i in range(constants.TILESIZE):
                for case in dungeon[j][i]:
                    if isinstance(case, Floor):
                        self.player = Player(((self.dungeonSize) // 2) * constants.TILESIZE + i, ((self.dungeonSize) // 2) * constants.TILESIZE + j, 100)
                        return