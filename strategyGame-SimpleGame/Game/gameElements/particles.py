from Game.gameElements.sprite import sprite
import random
class particles(sprite):
    LEFT = 0
    RIGHT = 1
    UP = 1
    DOWN = 0
    NONE = 2
    WHITE = None
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        if(particles.WHITE == None):
            particles.WHITE = []
            for index in range(0, 56):
                sprtPath = r"\resources\sprites\particle\white\\" + str(index) + ".png"
                particles.WHITE.append(self.loadImg(sprtPath))
        self.animationCount = random.randint(-1, 55)
        self.shuffleDir()

    def shuffleDir(self):
        self.xD =  random.choice([particles.RIGHT, particles.LEFT, particles.NONE])
        self.yD =  random.choice([particles.UP, particles.DOWN, particles.NONE])

    def outOfScreen(self):
        xBoundry = self.rect.x < 0 or (self.rect.x + self.rect.w) > self.sWidth
        yBoundry = self.rect.y < 0 or (self.rect.y + self.rect.h) > self.sHeight
        return xBoundry or yBoundry
    def update(self):
        if(self.nextAnimation(55, 100)):
            self.img = particles.WHITE[self.animationCount]
            if(self.xD ==  particles.RIGHT): self.rect.x += 1
            elif(self.xD ==  particles.LEFT): self.rect.x -= 1
            if(self.xD ==  particles.UP): self.rect.y -= 1
            elif(self.xD ==  particles.DOWN): self.rect.y += 1
            if(self.animationCount == 55 or self.outOfScreen()):
                self.shuffleDir()
