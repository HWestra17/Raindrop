import SpriteManager
from Sprite import Sprite

class Bullet(Sprite):
    speed = 8
    diameter = 10
    c = color(255,255,0)
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        if (self.x < 0 - self.diameter
        or self.x > width + self.diameter
        or self.y < 0 - self.diameter
        or self.y > height + self.diameter):
            SpriteManager.destroy(self)
