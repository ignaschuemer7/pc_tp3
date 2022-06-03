import random
from player import Player

class Gnomo(Player):
    def __init__(self, name, xy , face='G', hit_points=50):
        super().__init__(name, xy, face ,hit_points=hit_points)
        self.sword = False

    def damage(self):
        if self.face=='G':
            return random.randint(1,2) * 10 + 1
        elif self.face=='Ĝ':
            return random.randint(1,2) * 15 + 1
        elif self.face=='ğ':
            return random.randint(1,2) * 20 + 1