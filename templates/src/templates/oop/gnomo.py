import random
from player import Player

class Gnomo(Player):
    def __init__(self, name, xy , face='G', hit_points=50):
        super().__init__(name, xy, face ,hit_points=hit_points)
        self.sword = False

    def damage(self):
        return random.randint(1,2) * 10 + 1