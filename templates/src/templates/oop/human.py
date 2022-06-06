import random
from player import Player


class Human(Player):
    def __init__(self, name, xy,face='@',hit_points=500):
        super().__init__(name, xy, face ,hit_points=hit_points)
        self.weapon = False
        self.treasure = False
        self.tool = False 

    def damage(self) -> int:
        '''
        Determines the damage the player deals (with and without the sword).       

        Returns
        -------
            New player´s damage

            '''
        if self.weapon:
            return random.randint(1,2) * 20 + 5
        return random.randint(1,2) * 10 + 1

    def has_sword(self) -> bool:
        '''
        Determines whether or not the player has the sword

        '''
        self.weapon=True

    def __str__(self) -> str:
        '''
        
        '''
        return f"|Player: {self.name} |HP: {self.hp} |PickAxe: {self.tool} |Sword: {self.weapon} |Treasure: {self.treasure}"

