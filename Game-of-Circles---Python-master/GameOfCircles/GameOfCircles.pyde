import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Lobber import Lobber
from afterL import afterL
import SpriteManager
from Player import Player

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    print "Built with Processing version" + platform.python_version()
    size(500,500)
    player = Player(width / 2, height - 100, 1);
    SpriteManager.setPlayer(player)
    #SpriteManager.spawn(Enemy(100,100,2))
    #SpriteManager.spawn(Enemy(50, 50, enemyTeam))
    #SpriteManager.spawn(Enemy(150, 50, enemyTeam))
    #SpriteManager.spawn(Raindrop(150,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(100,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(200,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(250,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(450,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(40,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(60,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(160,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(130,50,enemyTeam))
    #SpriteManager.spawn(Raindrop(90,50,enemyTeam))
    #SpriteManager.spawn(JiggleBot(200,200,enemyTeam))
    #SpriteManager.spawn(ScreenSaverBot(100,100,enemyTeam))
    #SpriteManager.spawn(Lobber(100,100, enemyTeam))
    SpriteManager.spawn(afterL(15,50, enemyTeam))
    
def draw():
    background(0)    
    SpriteManager.animate()
        
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
