import random
from player import Player

class gnomo(Player):
    def __init__(self, name, xy , face='G', hit_points=50):
        super().__init__(name, xy, face ,hit_points=hit_points)
        self.weapon = None

    def damage(self):
        return random.random() * 10 + 1
