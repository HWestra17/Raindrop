import SpriteManager
from Sprite import Sprite

class BS(Sprite):
    diameter = 10
    c = color(0)
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        self.speed = 8
        
    def display(self):
        fill(self.c)
        rect(self.x, self.y, self.diameter, self.diameter)
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        if (self.x < 0 - self.diameter
        or self.x > width + self.diameter
        or self.y < 0 - self.diameter
        or self.y > height + self.diameter):
            SpriteManager.destroy(self)
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
