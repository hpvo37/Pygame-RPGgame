from Game.gameElements.sprite import sprite
from Game.gameElements.player import player

import pygame
import random

class map(sprite):
    COLLIDELIMIT = 18
    GRIDCOLOR = pygame.Color(0, 0, 0)
    
    #Grid dimensions
    GHEIGHT = 70
    GWIDTH = 70
    
    #Number of rows and Columns
    ROWCOUNT = 10
    COLUMNCOUNT = 15

    #Map Margin
    TOPMARGIN = 10
    LEFTMARGIN = 65

    FLOATINGT = None
    def __init__(self, mapData):
        super().__init__(0, 0, 0, 0)
        if(map.FLOATINGT == None):
            map.FLOATINGT = []
            map.FLOATINGT.append(r"\resources\sprites\map\tree1.png")
            map.FLOATINGT.append(r"\resources\sprites\map\1.png")
            map.FLOATINGT.append(r"\resources\sprites\map\2.png")
            map.FLOATINGT.append(r"\resources\sprites\map\3.png")
            map.FLOATINGT.append(r"\resources\sprites\map\4.png")
            map.FLOATINGT.append(r"\resources\sprites\map\5.png")
            map.FLOATINGT.append(r"\resources\sprites\map\6.png")
            map.FLOATINGT.append(r"\resources\sprites\map\7.png")
            map.FLOATINGT.append(r"\resources\sprites\map\8.png")
        self.tiles = []
        self.floatingTiles = []
        self.items = []
        ## Tile initialization (Can be used for the initialization of tiles in from  jsonData)
        # In that case map dimension can be access with no problem through map
        
        for i in range(map.ROWCOUNT):
            yPos = (map.GHEIGHT * i) 
            newRow = []
            for j in range(map.COLUMNCOUNT):
                xPos = (map.GWIDTH * j)
                if(mapData[i][j] < 0):
                    sprt = sprite(xPos, yPos, map.GWIDTH, map.GHEIGHT, map.FLOATINGT[(mapData[i][j] + 1) * -1])
                    self.floatingTiles.append(sprt)
                    newRow.append(tile(xPos, yPos, map.GWIDTH, map.GHEIGHT, 20))
                else: newRow.append(tile(xPos, yPos, map.GWIDTH, map.GHEIGHT, mapData[i][j]))
            self.tiles.append(newRow)

    def drawGridLines(self):
        yLimit = map.GHEIGHT * map.ROWCOUNT
        xLimit = map.GWIDTH * map.COLUMNCOUNT
        for rowNum in range(map.ROWCOUNT + 1):
            yLinePos = map.GHEIGHT * rowNum
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (0, yLinePos), (xLimit, yLinePos))
        for colNum in range(map.COLUMNCOUNT + 1):
            xLinePos = map.GWIDTH * colNum
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (xLinePos,  0), (xLinePos, yLimit))

    ## Can become part of model depending of our needs  ##
    def drawTileContent(self):
        for i in range(map.ROWCOUNT):
            for j in range(map.COLUMNCOUNT):
                self.tiles[i][j].draw()

    def collide(self, sprite):
        for row in self.tiles:
            for tile in row:
                if(tile.type <= map.COLLIDELIMIT and tile.collide(sprite)):
                    return True
        return False
    
    # Gets tile that has been clicked on
    def getSelectedTile(self, x, y):
        for row in self.tiles:
            for tile in row:
                if(tile.mouseInIt(x, y)): return tile
        return None

    def getTileAt(self, x, y):
        print("Grid Coordinates ROW: {" + str(y//map.GHEIGHT) + "} COLUMN: {" + str(x//map.GWIDTH) + "}")
        return self.tiles[y//map.GHEIGHT][x//map.GWIDTH]

    def getTiles(self):
        tileArray = []
        for row in self.tiles:
            tileArray += row
        return tileArray

    def draw(self):
        self.drawTileContent()
        #self.drawGridLines()
        for item in self.items:
            item.draw()

    def update(self):
        pass


class tile(sprite):
    BGCOLOR = pygame.Color(95, 111, 58)
    SBGCOLOR = pygame.Color(144, 159, 67)
    MAPTOPMARGIN = 0
    MAPLEFTMARGIN = 0

    TYPE = None
    
    def __init__(self, x, y, w, h, tType):
        super().__init__(x, y, w, h)
        if tile.TYPE == None:
            tile.TYPE = []
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\rock1.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\rock2.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\21.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\22.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\23.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\cave.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\24.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\water1.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\42.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\26.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\18.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\35.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\water.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\9.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\10.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\11.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\12.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\water2.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\tree2.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\25.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\grass.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\39.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\30.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\35.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\33.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\34.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\27.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\28.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\40.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\13.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\14.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\15.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\16.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\37.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\38.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\36.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\bridge.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\19.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\17.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\20.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\32.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\31.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\flower.png"))

        self.img = tile.TYPE[tType]
        self.type = tType


    def getCenter(self, w, h):
        x = self.rect.x + (self.rect.w - w)//2
        y = self.rect.y + (self.rect.h - h)//2
        return (x, y)

    def draw(self):
        self.drawImg()

    def update(self):
        pass
