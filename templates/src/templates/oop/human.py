import random
from player import Player


class Human(Player):
    def __init__(self, name, xy,face,hit_points):
        super().__init__(name, xy, face ,hit_points)
        '''
        Subclass used for player representation.

        Parameters
        ----------
        name : str
            Represents the player's name.
        
        xy : tuple
            Represents the player's position on the map.

        face : str
            Represents the player's representation on the map.

        hit_points : int
            Represents the player's life points.

    '''
        self.weapon = False #Determines if the player has the sword.
        self.treasure = False #Determines if the player has the treasure.
        self.tool = False #Determines if the player has the pickaxe

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

    def has_sword(self):
        '''
        Determines whether or not the player has the sword

        '''
        self.weapon=True

    def __str__(self) -> str:
        '''
        Prints on the screen the different methods of the class

        Returns
        -------
            Player interface

        '''
        return f"|Player: {self.name} |HP: {self.hp} |PickAxe: {self.tool} |Sword: {self.weapon} |Treasure: {self.treasure}"

class barbarian(Human):
    def __init__(self, name, xy,face='@',hit_points=350):
        super().__init__(name, xy, face ,hit_points=hit_points)

    def damage(self):
        if self.weapon:
            return random.randint(1,2) * 20 + 5
        return random.randint(1,2) * 10 + 1

class knight(Human):
    def __init__(self, name, xy,face='𓀝',hit_points=300):
        super().__init__(name, xy, face ,hit_points=hit_points)

    def damage(self):
            if self.weapon:
                return random.randint(1,2) * 25 + 6
            return random.randint(1,2) * 23 + 2
class ninja(Human):
    def __init__(self, name, xy,face='🀀',hit_points=250):
        super().__init__(name, xy, face ,hit_points=hit_points)

    def damage(self):
            if self.weapon:
                return random.randint(1,2) * 30 + 7
            return random.randint(1,2) * 20 + 3