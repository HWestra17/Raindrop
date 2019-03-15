import SpriteManager
from Sprite import Sprite

class Raindrop (Sprite):
     
    speed = 3
    diameter = 15
    c = color(0,0,255)
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.speed *= -1
            self.y = 0
