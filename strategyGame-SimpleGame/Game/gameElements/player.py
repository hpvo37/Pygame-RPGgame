import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.lifeBar import lifeBar

PLAYERHP = 100 

class player(sprite):
    RIGHT = 0
    LEFT = 1
    def __init__(self, x, y, attack, defense, skill, speed, xp, hp = PLAYERHP):
        super().__init__(x, y, 60, 44)
        self.hp = hp
        self.attackDamage = attack
        self.defense = defense
        self.speed = speed
        self.skill = skill
        self.xp = xp
        self.prevRect = self.rect.copy()

        self.idle = [self.loadImg(r"\resources\sprites\idle\00.png"), self.loadImg(r"\resources\sprites\idle\01.png"),
                     self.loadImg(r"\resources\sprites\idle\02.png"), self.loadImg(r"\resources\sprites\idle\03.png")]
        self.run = []
        self.run.append([self.loadImg(r"\resources\sprites\run\00.png"), self.loadImg(r"\resources\sprites\run\01.png"),
                                  self.loadImg(r"\resources\sprites\run\02.png"), self.loadImg(r"\resources\sprites\run\03.png"),
                                  self.loadImg(r"\resources\sprites\run\04.png"), self.loadImg(r"\resources\sprites\run\05.png")])
        self.run.append([self.loadImg(r"\resources\sprites\run\L00.png"), self.loadImg(r"\resources\sprites\run\L01.png"),
                                  self.loadImg(r"\resources\sprites\run\L02.png"), self.loadImg(r"\resources\sprites\run\L03.png"),
                                  self.loadImg(r"\resources\sprites\run\L04.png"), self.loadImg(r"\resources\sprites\run\L05.png")])
        self.attack = [self.loadImg(r"\resources\sprites\attack\00.png"), self.loadImg(r"\resources\sprites\attack\01.png"),
                       self.loadImg(r"\resources\sprites\attack\02.png"), self.loadImg(r"\resources\sprites\attack\03.png"),
                       self.loadImg(r"\resources\sprites\attack\04.png"), self.loadImg(r"\resources\sprites\attack\05.png")]
        self.destX = x
        self.destY = y
        self.img = self.idle[0]
        self.moving = False
        self.attacking = False
        self.standing = True
        self.lastMove = pygame.time.get_ticks()
        self.damage = False
        self.lifeBar =  lifeBar(self.rect, self.hp)
        self.alive = False
        self.xDir = "RIGHT"
        self.yDir = "DOWN"

    def moveTo(self, x, y):
        self.destX = x
        self.destY = y

    def move(self, origin, destinatination):
        distance = destinatination - origin
        moveSpeed = self.speed
        if(not (distance % self.speed == 0)):
            moveSpeed = distance % self.speed
        if(distance > 0):
            return moveSpeed
        else:
            return -moveSpeed
            
    def heal(self, healingPower):
        self.hp += healingPower
        if(self.hp > PLAYERHP):

            self.hp = PLAYERHP

    def perfAttack(self):
        if(not self.attacking):
            self.misssnd = self.loadsnd(r'\resources\sounds\effects\swordmiss.wav')
            self.misssnd.play()
            self.attacking = True
            self.standing = False
            self.animationCount = 0 

    def haveToMove(self):
        return self.destX != self.rect.x or self.destY != self.rect.y

    def receiveAttack(self, damage):
        self.hp -= damage
        self.painsnd = self.loadsnd(r'\resources\sounds\effects\pain.wav')
        self.painsnd.play()
        if(self.hp <= 0):
            self.alive = False
    
    def update(self):
        if(self.haveToMove()):
            self.prevRect = self.rect.copy()
            if(pygame.time.get_ticks() - self.lastMove >=  5):
                xMove = self.move(self.rect.x, self.destX)
                #Setting directions for updating process
                if(xMove >= 0): self.xDir = "RIGHT"
                else: self.xDir = "LEFT"
                self.rect.x += xMove
                yMove = self.move(self.rect.y, self.destY)
                self.rect.y += yMove
                if(yMove >= 0): self.xDir = "DOWN"
                else: self.xDir = "UP"
                self.lastMove = pygame.time.get_ticks()
            if(self.nextAnimation(5, 75)):
                if(self.destX >= self.rect.x): self.img = self.run[player.RIGHT][self.animationCount]
                else: self.img = self.run[player.LEFT][self.animationCount]
            if(not self.haveToMove()):
                self.standing = True
                self.animationCount = 0
        elif(self.attacking):
            if(self.nextAnimation(6, 75)):
                if(self.animationCount == 6):
                    self.standing = True
                    self.attacking =  False
                    self.animationCount = 0
                    self.damage =  True
                else:
                   self.img = self.attack[self.animationCount]
        else:
            if(self.nextAnimation(3, 75)):
                self.img = self.idle[self.animationCount]
        self.lifeBar.update(self.rect, self.hp)

    def draw(self):
        self.drawImg()
        self.lifeBar.draw()