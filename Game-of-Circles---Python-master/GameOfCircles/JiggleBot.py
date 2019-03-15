import SpriteManager
from Sprite import Sprite
#from Armored import Armored

class JiggleBot (Sprite):
     
    speed = 3
    diameter = 20
    c = color(88, 214, 141)
        
    def move(self):
        self.y += random (-self.speed, self.speed)
        self.x += random (-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
