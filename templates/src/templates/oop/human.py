import random
from player import Player


class Human(Player):
    def __init__(self, name, xy,face='@',hit_points=300):
        super().__init__(name, xy, face ,hit_points=hit_points)
        self.weapon = False
        self.treasure = False
        self.tool = False #seria el pico. si lo tiene o no

    def damage(self):
        if self.weapon:
            return random.randint(1,2) * 20 + 5
        return random.randint(1,2) * 10 + 1

    def has_sword(self)->bool:
        self.weapon=True

    def __str__(self):
        
        return f"|Player: {self.name} |HP: {self.hp} |PickAxe: {self.tool} |Sword: {self.weapon} |Treasure: {self.treasure}"

