from typing import Union


from human import Human
import player
import mapping


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
    
def is_in_dungeon(xy):
    if xy[0] in list(range(0,80)) and xy[1] in list(range(0,25)):
        return True
    return False


def attack(dungeon, player): # completar
    # completar
    raise NotImplementedError


def move_to(player: player.Player, location: tuple[numeric, numeric]):
    player.move_to(location)
    return player
    
def move_up(positionxy):
    positionxy=(positionxy[0],positionxy[1]-1)
    return positionxy

def move_down(positionxy):
    positionxy=(positionxy[0],positionxy[1]+1)
    return positionxy


def move_left(positionxy):
    positionxy=(positionxy[0]-1,positionxy[1])
    return positionxy


def move_right(positionxy):
    positionxy=(positionxy[0]+1,positionxy[1])
    return positionxy


#def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


#def descend_stair(dungeon: mapping.Dungeon, player: player.Player):#
    # completar
    raise NotImplementedError


#def pickup(dungeon: mapping.Dungeon , player: player.Player):
##    Human.tool=True
  #  return Human
