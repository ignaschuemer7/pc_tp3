import random
from player import Player


class Human(Player):
    def __init__(self, name, xy,face='@',hit_points=50):
        super().__init__(name, xy, face ,hit_points=hit_points)
        self.weapon = False
        self.treasure = False
        self.tool = False #seria el pico. si lo tiene o no

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def has_sword(self)->bool:
        return self.sword

