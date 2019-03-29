import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from Armored import Armored

class Enemy(Armored, Sprite):

    speed = 8
    diameter = 50
    c = color(10,25,255)

    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
