
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
    player1 = Human('gordo', mapping.Dungeon.find_free_tile(dungeon) ,'@',450)
    # initial locations may be random generated
    gnomo1 = Gnomo('gnomo', mapping.Dungeon.find_free_tile(dungeon) ,'G',50)
    
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

        print('Level:',dungeon.level, str(player1))
        
        dungeon.render(player1,gnomo1)

        #print(mapping.Level.are_connected(dungeon,player1.loc(), pickaxe.loc()))
       
        position_xy_gnomo=gnomo1.loc()

        key = msvcrt.getch().decode('UTF-8')

        
        position_xy_human=player1.loc()

        if key=="w":
            position_xy_human=move_up(position_xy_human)
        elif key=="s":
            position_xy_human=move_down(position_xy_human)
        elif key=="d":
            position_xy_human=move_right(position_xy_human)
        elif key=="a":
            position_xy_human=move_left(position_xy_human)

    
        if is_in_dungeon(position_xy_human) and position_xy_human!=gnomo1.loc():
            if dungeon.is_walkable(position_xy_human) :
                player1=move_to(player1,position_xy_human)
            elif player1.tool:
                dungeon.dig(position_xy_human)
                player1=move_to(player1,position_xy_human)
        elif is_in_dungeon(position_xy_human) and dungeon.is_walkable(position_xy_human):
            #el jugador se movio a la posicion del gnomo y lo ataco
            #ataque
            print("ataco el jugador")
            attack(dungeon, player1, gnomo1)

        position_xy_human=player1.loc()
        
        position_xy_gnomo=move_gnomo(gnomo1.loc(),dungeon)

        if position_xy_gnomo!=position_xy_human:
            gnomo1.move_to(position_xy_gnomo)
        else:
            #ataque
            #ataque del momo hacia el jugador
            print("ataco el gnomo")
            attack(dungeon, gnomo1, player1)
        
        
        #condiciones si el juegador agarra los items
        mapping.Dungeon.get_items(dungeon,player1.loc())

        if player1.loc()==pickaxe.loc():
            player1.tool=True
        
        if player1.loc()==sword.loc():
            player1.has_sword=True
        
        if player1.loc()==amulet.loc():
            player1.treasure=True

        #escaleras
        if mapping.Dungeon.loc(dungeon,player1.loc()).face =='<':
            dungeon.level-=1
        elif mapping.Dungeon.loc(dungeon,player1.loc()).face =='>':
            dungeon.level+=1


        #si se muere el jugador, termina el juego
        if player1.hp<=0:
            player1.kill()
        if not player1.alive:
            break
        #si se muere el gnomo, le cambiamos el caracter, dejamos el cadaver en el mapa
        if gnomo1.hp<=0:
            gnomo1.kill()
            gnomo1.face='O'
        
        
        
        
        
        
    if player1.treasure and player1.alive:
        print("You Win!!")
    else:
        print("You Lose..Try again!")
        
        
        

        

        
        
        
        

    # Salió del loop principal, termina el juego
