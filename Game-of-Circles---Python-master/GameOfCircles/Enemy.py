import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from Armored import Armored
from ArmoredS import ArmoredS

class Enemy(Armored, Sprite):

    speed = 8
    diameter = 50
    c = color(10,25,25)

    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
