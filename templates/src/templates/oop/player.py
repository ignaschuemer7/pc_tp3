
class Player:
    def __init__(self, name, xy, face, hit_points=50):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points
        self.face = face
        self.alive = True
 
    def loc(self):
        return self.x, self.y

    def move_to(self, xy):
        self.x, self.y = xy
        
    def recive_damage(self,damage):
        self.hp = self.hp - damage
        

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc()}', '{self.hp}')"
        
    def kill(self):
        self.hp=0
        self.alive = False
