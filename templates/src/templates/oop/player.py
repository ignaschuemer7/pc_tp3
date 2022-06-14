
class Player:
    def __init__(self, name, xy, face, hit_points):
        '''
        Class used for generate the player and the NPCs (gnomo).

        Parameters
        ----------
        name : str
            Represents the name.
        
        xy : tuple
            Represents the position on the map.

        face : str
            Is the character used to represent the object on the screen.

        hit_points : int
            Represents the life points.

    '''
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points
        self.face = face
        self.alive = True
 
    def loc(self):
        '''
        Return the object's position.

        '''
        return self.x, self.y

    def move_to(self, xy):
        '''
        Defines the position of the object.
        
        '''
        self.x, self.y = xy
        
    def recive_damage(self,damage):
        '''
        Interprets when the object takes damage.

        '''
        self.hp = self.hp - damage
        
    def __repr__(self):
        '''
        Represent a class's objects as a string.
        
        '''
        return f"Player('{self.name}', '{self.loc()}', '{self.hp}')"
        
    def kill(self):
        '''
        Interprets the death when it runs out of life points.

        '''
        self.hp=0
        self.alive = False
