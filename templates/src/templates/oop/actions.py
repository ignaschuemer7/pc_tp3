from typing import Union


from human import Human
import player
import gnomo
import random
import game


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


def attack(dungeon, do_damage: player.Player, recive_damage: player.Player):
    generate_damage=do_damage.damage()
    recive_damage=recive_damage.recive_damage(generate_damage)
    
    


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

def move_gnomo(position_xy_gnomo,dungeon):
    
    while True:

            old_position=position_xy_gnomo

            position_xy_gnomo=random.choice([move_up(position_xy_gnomo),move_down(position_xy_gnomo),
            move_right(position_xy_gnomo),move_left(position_xy_gnomo)])

            if is_in_dungeon(position_xy_gnomo) and dungeon.is_walkable(position_xy_gnomo):
                break
            position_xy_gnomo=old_position
            
    return position_xy_gnomo


#def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
   # raise NotImplementedError


#def descend_stair(dungeon: mapping.Dungeon, player: player.Player):#
    # completar
   # raise NotImplementedError


#def pickup(dungeon: mapping.Dungeon , player: player.Player):
##    Human.tool=True
  #  return Human
