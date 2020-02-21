import random
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.lifeBar import lifeBar
from Game.gameElements.item import item

PATTACKDURATION = 450

WORMHP = 30
WORMATTACK = 5

DRAGONATTACK = 10
DRAGONSPEED = 10
DRAGONHP = 70
RIGHT = 1
LEFT = 0

class enemy(sprite):
    def __init__(self, x, y, w, h, hp, hitInterval):
        super().__init__(x, y, w, h)

        self.hp = hp
        self.hitInterval = hitInterval
        self.lifeBar = lifeBar(self.rect, self.hp)
        self.animationCount = 0
        
        self.isDying =  False
        self.isAttacking =  False
        self.alive =  True

        self.lastAttack = pygame.time.get_ticks()
        self.lastHit = pygame.time.get_ticks()
        self.lastDamage = pygame.time.get_ticks()
        
    def hitAgain(self):
        if(pygame.time.get_ticks() - self.lastHit >= self.hitInterval):
            self.lastHit = pygame.time.get_ticks()
            return True
        else: return False

    def receiveAttack(self, damage):
        if(pygame.time.get_ticks() - self.lastDamage >= PATTACKDURATION):
            self.lastDamage = pygame.time.get_ticks()
            self.hp -= damage
            self.attacksnd = self.loadsnd(r'\resources\sounds\effects\swordhit.wav')
            self.attacksnd.play()
        if(self.hp <= 0):
            self.animationCount = 0
            self.isDying = True
            self.isIdle = False
            self.isAtticking =  False
            self.dyingsnd = self.loadsnd(r'\resources\sounds\effects\monsterpain.wav')
            self.dyingsnd.play()
    def dropItem(self):
        dropPossibility =  random.randint(0, 100)
        if(dropPossibility > 50):
            return item(self.rect)
        else: return None

    def draw(self):
        self.lifeBar.draw()
        self.drawImg()

class dragon(enemy):

    def __init__(self, x, y, w, h, map, attack = DRAGONATTACK):
        super().__init__(x, y, w, h, DRAGONHP, 1000)
        self.walk = []
        self.walk.append([self.loadImg(r"\resources\sprites\Dragon\walk\L00.png"), self.loadImg(r"\resources\sprites\Dragon\walk\L01.png")])
        self.walk.append([self.loadImg(r"\resources\sprites\Dragon\walk\00.png"), self.loadImg(r"\resources\sprites\Dragon\walk\01.png")])

        self.attackDamage = attack
        self.attack = []
        self.attack.append([self.loadImg(r"\resources\sprites\Dragon\attack\L00.png"), self.loadImg(r"\resources\sprites\Dragon\attack\L01.png")])
        self.attack.append([self.loadImg(r"\resources\sprites\Dragon\attack\00.png"), self.loadImg(r"\resources\sprites\Dragon\attack\01.png")])

        self.isWalking = True

        self.map = map

        self.direction = random.choice([LEFT, RIGHT])

    def isOutofScreen(self):
        return (self.rect.x + self.rect.w >= sprite.sWidth)  or (self.rect.x <= 0)
    
    def update(self):
        self.lifeBar.update(self.rect, self.hp)
        self.lifeBar.update(self.rect, self.hp)
        if(pygame.time.get_ticks() - self.lastAttack >= 4000):  
            self.lastAttack = pygame.time.get_ticks()
            self.isAttacking = True
            self.animationCount = -1

        if(self.isDying):
            self.alive = False
        elif(self.isWalking):
            if(self.nextAnimation(1, 125)):
                if(self.direction == RIGHT):
                    self.rect.x += DRAGONSPEED
                    if(self.map.collide(self) or self.isOutofScreen()):
                        self.direction = LEFT
                if(self.direction == LEFT):
                    self.rect.x -= DRAGONSPEED
                    if(self.map.collide(self) or self.isOutofScreen()):
                        self.direction = RIGHT
                if(self.isAttacking):
                    self.img = self.attack[self.direction][self.animationCount]
                    if(pygame.time.get_ticks() - self.lastAttack >= 2000): self.isAttacking = False
                elif(self.isWalking): self.img = self.walk[self.direction][self.animationCount]

                

class worm(enemy):
    def __init__(self, x, y, w, h, attack = WORMATTACK):
        super().__init__(x, y, w, h, WORMHP, 1000)
        self.attackDamage = attack
        self.idle = [self.loadImg(r"\resources\sprites\worm\idle\00.png"), self.loadImg(r"\resources\sprites\worm\idle\01.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\02.png"), self.loadImg(r"\resources\sprites\worm\idle\03.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\04.png"), self.loadImg(r"\resources\sprites\worm\idle\05.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\06.png"), self.loadImg(r"\resources\sprites\worm\idle\07.png")]
        self.idleDirt = self.loadImg(r"\resources\sprites\worm\dirt\idle.png");

        self.dying = [self.loadImg(r"\resources\sprites\worm\dying\00.png"), self.loadImg(r"\resources\sprites\worm\dying\01.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\02.png"), self.loadImg(r"\resources\sprites\worm\dying\03.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\04.png"), self.loadImg(r"\resources\sprites\worm\dying\05.png")]

        self.dyingDirt = [self.loadImg(r"\resources\sprites\worm\dying\d00.png"), self.loadImg(r"\resources\sprites\worm\dying\d01.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\d02.png"), self.loadImg(r"\resources\sprites\worm\dying\d03.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\d04.png"), self.loadImg(r"\resources\sprites\worm\dying\d05.png")]
        self.attack = [self.loadImg(r"\resources\sprites\worm\attacking\00.png"), self.loadImg(r"\resources\sprites\worm\attacking\01.png"),
                       self.loadImg(r"\resources\sprites\worm\attacking\00.png"), self.loadImg(r"\resources\sprites\worm\attacking\01.png")]

        self.dirt = self.idleDirt
        self.hp = WORMHP
        self.img = self.idle[0]

        #Tile Data
        #Position in tiles
        
        self.isIdle = True

            
    def update(self):
        self.lifeBar.update(self.rect, self.hp)
        if(pygame.time.get_ticks() - self.lastAttack >= 2000 and not self.isDying):
            self.lastAttack = pygame.time.get_ticks()
            self.animationCount = -1
            self.isAttacking = True
            self.isIdle = False
        if(self.isIdle):
            if(self.nextAnimation(7, 100)):
                self.img = self.idle[self.animationCount]
                self.dirt = self.idleDirt
        elif(self.isDying):
            if(self.nextAnimation(6, 100)):
                if(self.animationCount == 6):
                    self.isDying = False
                    self.alive = False
                else:
                    self.img = self.dying[self.animationCount]
                    self.dirt = self.dyingDirt[self.animationCount]
        elif(self.isAttacking):
            if(self.nextAnimation(4, 100)):
                if(self.animationCount == 4):
                    self.isAttacking = False
                    self.isIdle = True
                else:
                    self.img = self.attack[self.animationCount]
    def draw(self):
        self.lifeBar.draw()
        self.drawImg()
        sprite.screen.blit(self.dirt, self.rect)

