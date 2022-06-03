from typing import Tuple, Union


from human import Human
import player
import mapping
import random
import items


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
    
def is_in_dungeon(xy:tuple) -> bool:
    '''
    Analyze if the player's movement is within the limits of the map.

    Parameters
    ----------
    xy : tuple
        Represents player movement.
   
    Returns
    -------
        True or False

    '''  
    if xy[0] in list(range(0,80)) and xy[1] in list(range(0,25)):
        return True
    return False


def attack(do_damage, recive_damage):
    '''
    
    '''
    generate_damage=do_damage.damage()
    recive_damage.recive_damage(generate_damage)
    
def move_to(player: player.Player, location: tuple[numeric, numeric]):
    player.move_to(location)
    return player
    
def move_up(positionxy):
    '''
    Makes an upward movement.

    Parameters
    ----------
    positionxy : tuple
        Represents the player's position in the dungeon.
   
    Returns
    -------
        New positionxy

    '''
    positionxy=(positionxy[0],positionxy[1]-1)
    return positionxy

def move_down(positionxy):
    '''
    Makes a downward movement.

    Parameters
    ----------
    positionxy : tuple
        Represents the player's position in the dungeon.
   
    Returns
    -------
        New positionxy
        
    '''
    positionxy=(positionxy[0],positionxy[1]+1)
    return positionxy


def move_left(positionxy: tuple) -> tuple:
    '''
    Make a movement to the left. 

    Parameters
    ----------
    positionxy : tuple
        Represents the player's position in the dungeon.
   
    Returns
    -------
        New positionxy

    '''
    positionxy=(positionxy[0]-1,positionxy[1])
    return positionxy


def move_right(positionxy: tuple) -> tuple:
    '''
    Make a movement to the right. 

    Parameters
    ----------
    positionxy : tuple
        Represents the player's position in the dungeon.
   
    Returns
    -------
        New positionxy

    '''
    positionxy=(positionxy[0]+1,positionxy[1])
    return positionxy

def move_gnomo(position_xy_gnomo: tuple,dungeon) -> tuple:
    
    while True:

            old_position=position_xy_gnomo

            position_xy_gnomo=random.choice([move_up(position_xy_gnomo),move_down(position_xy_gnomo),
            move_right(position_xy_gnomo),move_left(position_xy_gnomo)])

            if is_in_dungeon(position_xy_gnomo) and dungeon.is_walkable(position_xy_gnomo):
                break
            #if it can't move to either side, it will cut the loop
            if (not dungeon.is_walkable(move_up(position_xy_gnomo)) 
            and not dungeon.is_walkable(move_down(position_xy_gnomo)) 
            and not dungeon.is_walkable(move_right(position_xy_gnomo)) 
            and not dungeon.is_walkable(move_left(position_xy_gnomo))):
                position_xy_gnomo=old_position
                break
            position_xy_gnomo=old_position
            
    return position_xy_gnomo


def climb_stair(dungeon):
    dungeon.level-=1

def descend_stair(dungeon):
    dungeon.level+=1

def stairs(dungeon,player1):
    if dungeon.loc(player1.loc()).face =='<':
            climb_stair(dungeon)
    elif dungeon.loc(player1.loc()).face =='>':
            descend_stair(dungeon)

def pickup(dungeon,player1,pickaxe,sword,amulet):
    dungeon.get_items(player1.loc())
    if player1.loc()==pickaxe.loc() and dungeon.level==0:
            player1.tool=True
    elif player1.loc()==sword.loc() and dungeon.level==1:
            player1.has_sword()
    elif player1.loc()==amulet.loc() and dungeon.level==2:
            player1.treasure=True

def human_is_dead(player1):
    if player1.hp<=0:
        player1.kill()
    if not player1.alive:
        return True
    return False

def gnomo_is_dead(gnome):
    if gnome.hp<=0:
            gnome.kill()
            return True
    return False

def player_movements(key,position_xy_human):
    if key=="w":
        position_xy_human=move_up(position_xy_human)
    elif key=="s":
        position_xy_human=move_down(position_xy_human)
    elif key=="d":
        position_xy_human=move_right(position_xy_human)
    elif key=="a":
        position_xy_human=move_left(position_xy_human)
    return position_xy_human

def gnomo_move_and_attack(player1,gnome,position_xy_human,position_xy_gnomo):
    if position_xy_gnomo!=position_xy_human and gnome.alive:
        gnome.move_to(position_xy_gnomo)
    elif gnome.alive:
        #Gnome attack towards Player
        attack(gnome, player1)

def player_move_and_attack(dungeon,player1,gnome,position_xy_human,position_xy_gnomo):
    if is_in_dungeon(position_xy_human) and position_xy_human!=position_xy_gnomo:
        if dungeon.is_walkable(position_xy_human) :
            player1=move_to(player1,position_xy_human)
        elif player1.tool:
            dungeon.dig(position_xy_human)
            player1=move_to(player1,position_xy_human)
    elif is_in_dungeon(position_xy_human) and dungeon.is_walkable(position_xy_human):
        #Player attack towards Gnome
        attack(player1, gnome)
        
def select_gnome(level,gnomo1,gnomo2,gnomo3):
    if level == 0:
        gnome=gnomo1
    if level == 1:
        gnome=gnomo2
    if level == 2:
        gnome=gnomo3
    return gnome
