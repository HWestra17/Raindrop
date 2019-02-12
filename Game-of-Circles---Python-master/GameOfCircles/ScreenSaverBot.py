class ScreenSaverBot:
     
    xspeed = 3
    yspeed = 3
    diameter = 15
    c = color(0,255,0)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self .x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()