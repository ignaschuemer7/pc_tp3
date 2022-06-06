import random
from player import Player

class Gnomo(Player):
    def __init__(self, name, xy , face, hit_points):
        super().__init__(name, xy, face ,hit_points)
        self.sword = False

    def __str__(self) -> str:
        return f"Enemy: {self.name} |HP: {self.hp}"
class kobold(Gnomo):
    def __init__(self, name, xy , face='G', hit_points=50):
        super().__init__(name, xy, face ,hit_points=hit_points)
    
    def damage(self):
        return random.randint(1,2) * 10 + 1

class knoker(Gnomo):
    def __init__(self, name, xy , face='Ĝ', hit_points=100):
        super().__init__(name, xy, face ,hit_points=hit_points)
   
    def damage(self):
        return random.randint(1,2) * 15 + 1

class spriggan(Gnomo):
    def __init__(self, name, xy , face='ğ', hit_points=150):
        super().__init__(name, xy, face ,hit_points=hit_points)
    
    def damage(self):
        return random.randint(1,2) * 20 + 1  
    
