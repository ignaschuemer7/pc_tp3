from typing import Union


numeric = Union[float, int]


class Item:
    def __init__(self, name, xy, fc, type):
        self.name = name
        self.face = fc
        self.type = type
        self.x, self.y = xy

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"


class Sword(Item):
    def __init__(self, name: str, fc: str, min_dmg: numeric, max_dmg: numeric):
        super().__init__(name, fc, 'weapon')
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg


class Amulet(Item):
    def __init__(self, name: str, fc: str):
        super().__init__(name, fc, 'treasure')


class PickAxe(Item):
    def __init__(self, name: str, xy,fc="("):
        super().__init__(name,xy,fc, 'tool')
