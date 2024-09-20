from direct.showbase.ShowBase import ShowBase
from map import Mapmanager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        x,y,z = self.land.loadland("land.txt")
        self.hero = Hero((x//2,y//2,7+9),self.land)
game = Game()
game.run()