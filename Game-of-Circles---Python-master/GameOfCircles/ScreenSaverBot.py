import SpriteManager
from Sprite import Sprite

class ScreenSaverBot (Sprite):
     
    xspeed = 3
    yspeed = 3
    diameter = 15
    c = color(0,255,0)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self .x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
