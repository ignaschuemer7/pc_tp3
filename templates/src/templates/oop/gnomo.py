import random
from player import Player

class Gnomo(Player):
    def __init__(self, name, xy , face, hit_points):
        super().__init__(name, xy, face ,hit_points)
        '''
        Subclass used for gnomo representation.

        Parameters
        ----------
        name : str
            Represents the gnomo's name.
        
        xy : tuple
            Represents the gnomo's position on the map.

        face : str
            Represents the gnomo's representation on the map.

        hit_points : int
            Represents the gnomo's life points.

        '''
        self.sword = False #The gnomo never has the sword

    def __str__(self) -> str:
        '''
        Prints on the screen the different methods of the class.

        Returns
        -------
            Gnomo interface (str).
        '''
        return f"Enemy: {self.name} |HP: {self.hp}"
class kobold(Gnomo):
    def __init__(self, name, xy , face='G', hit_points=50):
        super().__init__(name, xy, face ,hit_points=hit_points)
    
    def damage(self):
        '''
        Determines the damage the gnomo deals.       

        Returns
        -------
            New gnomo´s damage (int).
        '''
        return random.randint(1,2) * 10 + 1

class knoker(Gnomo):
    def __init__(self, name, xy , face='Ĝ', hit_points=100):
        super().__init__(name, xy, face ,hit_points=hit_points)
   
    def damage(self):
        '''
        Determines the damage the gnomo deals.       

        Returns
        -------
            New gnomo´s damage (int).
        '''
        return random.randint(1,2) * 15 + 1

class spriggan(Gnomo):
    def __init__(self, name, xy , face='ğ', hit_points=150):
        super().__init__(name, xy, face ,hit_points=hit_points)
    
    def damage(self):
        '''
        Determines the damage the gnomo deals.       

        Returns
        -------
            New gnomo´s damage (int).
        '''
        return random.randint(1,2) * 20 + 1  
    
