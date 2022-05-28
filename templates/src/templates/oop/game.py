from re import X
import time
import mapping
import magic

import random
from human import Human
from gnomo import Gnomo
from items import Item
from actions import *
import msvcrt


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
    level = 0
    player = Human('player',(12,12),'@')
    # initial locations may be random generated
    gnomo = Gnomo('gnomo',(13,16),'G',50)

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render(player,gnomo)

        # read key

        
        #key = msvcrt.getch().decode('UTF-8')
        key=input("ingrese letra")
        # Hacer algo con keys:
        # move player and/or gnomes
        positionxy=player.loc()
        if key=="w":
            positionxy=move_up(positionxy)
        elif key=="s":
            positionxy=move_down(positionxy)
        elif key=="d":
            positionxy=move_right(positionxy)
        elif key=="a":
            positionxy=move_left(positionxy)
        
        if dungeon.is_walkable(positionxy) and is_in_dungeon(positionxy):
            player=move_to(player,positionxy)
        
        
        

    # Salió del loop principal, termina el juego
