
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
    player1 = Human('player', mapping.Dungeon.find_free_tile(dungeon) ,'@')
    # initial locations may be random generated
    gnomo = Gnomo('gnomo', mapping.Dungeon.find_free_tile(dungeon) ,'G',50)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    turns = 0

    pickaxe=items.PickAxe("pickacke",mapping.Dungeon.find_free_tile(dungeon))
    sword=items.Sword("sword",mapping.Dungeon.find_free_tile(dungeon))
    amulet=items.Amulet("amulet",mapping.Dungeon.find_free_tile(dungeon))

    mapping.Dungeon.add_item(dungeon,pickaxe, pickaxe.loc(),1)

    mapping.Dungeon.add_item(dungeon,sword, sword.loc(),2)

    mapping.Dungeon.add_item(dungeon,amulet, amulet.loc(),3)
    
  

    while dungeon.level >= 0:
        turns += 1
        # render map
        
        dungeon.render(player1,gnomo)
        
        # read key

        position_xy_gnomo=gnomo.loc()

        key = msvcrt.getch().decode('UTF-8')
        #key=input("ingrese letra")
        # Hacer algo con keys:
        # move player and/or gnomes
        
        position_xy_human=player1.loc()

        if key=="w":
            position_xy_human=move_up(position_xy_human)
        elif key=="s":
            position_xy_human=move_down(position_xy_human)
        elif key=="d":
            position_xy_human=move_right(position_xy_human)
        elif key=="a":
            position_xy_human=move_left(position_xy_human)

    
        if is_in_dungeon(position_xy_human):
            if dungeon.is_walkable(position_xy_human):
                player1=move_to(player1,position_xy_human)
            elif player1.tool:
                dungeon.dig(position_xy_human)
                player1=move_to(player1,position_xy_human)


        move_gnomo(gnomo,position_xy_gnomo,dungeon)

        mapping.Dungeon.get_items(dungeon,player1.loc())
        #condiciones si el juegador agarra los items
        if player1.loc()==pickaxe.loc():
            player1.tool=True
        
        if player1.loc()==sword.loc():
            player1.has_sword
        
        if player1.loc()==amulet.loc():
            player1.treasure=True

        if mapping.Dungeon.loc(dungeon,player1.loc()).face =='<':
            dungeon.level-=1
        elif mapping.Dungeon.loc(dungeon,player1.loc()).face =='>':
            dungeon.level+=1
        
        
        
    if player1.treasure==True:
        print("You Win!!")
    else:
        print("You Lose..Try again!")
        
        
        

        

        
        
        
        

    # Salió del loop principal, termina el juego
