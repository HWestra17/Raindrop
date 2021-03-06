mark = 0
wait = 300
go = True
from Bullet import Bullet
from Sprite import Sprite
from Player import Player
import SpriteManager
from Enemy import Enemy

class Lobber (Sprite):
    
    speed = 5
    xspeed = 4
    diameter = 50
    c = color(101,5,3)
    
    def _init_(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
    
    
    def move(self):
        self.x += self.speed
        
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
    def aim(self, target):
        
        xDist = self.x - target.x
        yDist = self.y - target.y
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xVec = -xDist / 2 * .01
        yVec = -yDist / 2 * .01
        return PVector(xVec, yVec)
        return PVector(0,10)
    
    def fire(self, vector):
        global go, mark, wait
        if (millis() - mark > wait):
            go = not go
            mark = millis()
        
        if self.x < 0 or self.x > width:
            self.speed *= -1   
        
        if(go):
            go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
