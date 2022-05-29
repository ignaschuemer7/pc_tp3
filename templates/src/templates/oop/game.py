
from re import X
import time
import mapping


import random
from human import Human
from gnomo import Gnomo
import items
from actions import *
import msvcrt
import player




ROWS = 25
COLUMNS = 80
def init_game():
    dungeon = Dungeon(ROWS,COLUMNS, 3)
    character = choose_character()
    return dungeon,character

def choose_caracter():
    print("select yor cacarcter")
    print("1_Barbarian")

    choice = input("input the choice")

if __name__ == "__main__":
    # initial parameters
    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    level = 0
    player = Human('player', mapping.Dungeon.find_free_tile(dungeon) ,'@')
    # initial locations may be random generated
    gnomo = Gnomo('gnomo', mapping.Dungeon.find_free_tile(dungeon) ,'G',50)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    turns = 0

    pickAxe=items.PickAxe("pickAxe",mapping.Dungeon.find_free_tile(dungeon))
    #mapping.Level.add_item(items.PickAxe,mapping.Dungeon.find_free_tile(dungeon))
    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render(player,gnomo,pickAxe)
        
        # read key

        position_xy_gnomo=gnomo.loc()

        #key = msvcrt.getch().decode('UTF-8')
        key=input("ingrese letra")
        # Hacer algo con keys:
        # move player and/or gnomes
        
        position_xy_human=player.loc()

        if key=="w":
            position_xy_human=move_up(position_xy_human)
        elif key=="s":
            position_xy_human=move_down(position_xy_human)
        elif key=="d":
            position_xy_human=move_right(position_xy_human)
        elif key=="a":
            position_xy_human=move_left(position_xy_human)
        
        if dungeon.is_walkable(position_xy_human) and is_in_dungeon(position_xy_human):
            player=move_to(player,position_xy_human)
        
        

        

        
        
        
        

    # Salió del loop principal, termina el juego
