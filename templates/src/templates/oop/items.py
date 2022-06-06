from typing import Union


numeric = Union[float, int]


class Item:
    def __init__(self, name, xy, fc, type):
        '''
        Subclass used for items representation.

        Parameters
        ----------
        name : str
            Represents the items's name.
        
        xy : tuple
            Represents the items's position on the map.

        face : str
            Represents the items's representation on the map.

        type : int
            Represents the item's type.

        '''
        self.name = name 
        self.face = fc
        self.type = type
        self.x, self.y = xy

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"

    def loc(self):
        return self.x, self.y


class Sword(Item):
    def __init__(self, name: str, xy, fc: str='/', min_dmg: numeric=10, max_dmg: numeric=20):
        super().__init__(name, xy, fc,'weapon')
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg


class Amulet(Item):
    def __init__(self, name: str,xy, fc='"'):
        super().__init__(name, xy, fc,'treasure')


class PickAxe(Item):
    def __init__(self, name: str,xy,fc="("):
        super().__init__(name,xy,fc,'tool')
