from typing import Tuple, Union


from human import Human
import player
import random



numeric = Union[int, float]
    
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

def move_gnomo(position_xy_gnomo: tuple,position_xy_human: tuple,dungeon,pickaxe,amulet,sword,movements=[]) -> tuple:
    
    while True:

            old_position=position_xy_gnomo

            if position_xy_human[0]>position_xy_gnomo[0] and 'right' not in movements:
                position_xy_gnomo=move_right(position_xy_gnomo)
                movements.append('right')
            elif position_xy_human[0]<position_xy_gnomo[0] and 'left' not in movements:
                position_xy_gnomo=move_left(position_xy_gnomo)
                movements.append('left')  
            elif position_xy_human[1]>position_xy_gnomo[1] and 'down' not in movements:
                position_xy_gnomo=move_down(position_xy_gnomo)
                movements.append('down')
            elif position_xy_human[1]<position_xy_gnomo[1] and 'up' not in movements:
                position_xy_gnomo=move_up(position_xy_gnomo)
                movements.append('up')  
            else:
                position_xy_gnomo=random.choice([move_up(position_xy_gnomo),
                move_down(position_xy_gnomo),move_right(position_xy_gnomo),move_left(position_xy_gnomo)])

            if (is_in_dungeon(position_xy_gnomo) 
                and dungeon.is_walkable(position_xy_gnomo) 
                and position_xy_gnomo!=pickaxe.loc()
                and position_xy_gnomo!=amulet.loc()
                and position_xy_gnomo!=sword.loc()):
                break
            #if it can't move to either side, it will cut the loop
            elif (not dungeon.is_walkable(move_up(position_xy_gnomo)) 
                and not dungeon.is_walkable(move_down(position_xy_gnomo)) 
                and not dungeon.is_walkable(move_right(position_xy_gnomo)) 
                and not dungeon.is_walkable(move_left(position_xy_gnomo))):
                position_xy_gnomo=old_position
                break
            position_xy_gnomo=old_position      
    return position_xy_gnomo
def climb_stair(dungeon):
    '''
    Produces a change to the previous dungeon when the player climbs the stairs.

    '''
    dungeon.level-=1
    

def descend_stair(dungeon):
    '''
    Produces a change to the next dungeon when the player climbs the stairs.

    '''
    dungeon.level+=1

    

def stairs(dungeon,player1):
    '''
    Determines when the player goes up or down the stairs.

    '''
    if dungeon.loc(player1.loc()).face =='<':
            climb_stair(dungeon)
    elif dungeon.loc(player1.loc()).face =='>':
            descend_stair(dungeon)

def pickup(dungeon,player1,pickaxe,sword,amulet):
    '''
    Determines that the player has collected an item.

    '''
    dungeon.get_items(player1.loc())
    if player1.loc()==pickaxe.loc() and dungeon.level==0:
            player1.tool=True
    elif player1.loc()==sword.loc() and dungeon.level==1:
            player1.has_sword()
    elif player1.loc()==amulet.loc() and dungeon.level==2:
            player1.treasure=True

def human_is_dead(player1):
    '''
    Changes the Player's status to dead when it loses all its HP.

    '''
    if player1.hp<=0:
        player1.kill()
    if not player1.alive:
        return True
    return False

def gnomo_is_dead(gnome):
    '''
    Changes the Gnome's status to dead when it loses all its HP.

    '''
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
    '''
    Puts all the Gnomes in their corresponding level.
    
    '''
    if level == 0:
        gnome=gnomo1
    if level == 1:
        gnome=gnomo2
    if level == 2:
        gnome=gnomo3
    return gnome

def gnomo_unlocks(dungeon,gnome,player1,amulet,sword):
    if gnomo_is_dead(gnome) and dungeon.level==0:
            gnome.face='%'
    if gnomo_is_dead(gnome) and player1.treasure==False and dungeon.level==2:
        gnome.face='%'
        dungeon.add_item(amulet, amulet.loc(),3)
    if gnomo_is_dead(gnome) and player1.weapon==False and dungeon.level==1:
        gnome.face='%'
        dungeon.add_item(sword, sword.loc(),2)
