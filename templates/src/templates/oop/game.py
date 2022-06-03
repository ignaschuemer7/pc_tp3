
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
    player1 = Human('gordo', dungeon.find_free_tile() ,'@',300)
    # initial locations may be random generated
    gnomo1 = Gnomo('gnomo', dungeon.find_free_tile() ,'G',50)
    gnomo2 = Gnomo('gnomo', dungeon.find_free_tile() ,'Ĝ',100)
    gnomo3 = Gnomo('gnomo', dungeon.find_free_tile() ,'ğ',200)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    turns = 0
    pickaxe=items.PickAxe("pickacke",dungeon.find_free_tile())
    sword=items.Sword("sword",dungeon.find_free_tile())
    amulet=items.Amulet("amulet",dungeon.find_free_tile())

    dungeon.add_item(pickaxe, pickaxe.loc(),1)
    dungeon.add_item(sword, sword.loc(),2)
    dungeon.add_item(amulet, amulet.loc(),3)
    
    while dungeon.level >= 0:
        
        #if gnomo3.face=='%' and len(mapping.items)==2:
         #   dungeon.add_item(amulet, amulet.loc(),3)
        #nivel 0, 1 gnomo, nivel 1, 2 gnomos y nivel 3, 3 gnomos

        turns += 1

        #mostrar valores en pantalla
        print('Level:',dungeon.level, str(player1))

        #segun el nivel, cada gnomo
        
        if dungeon.level == 0:
            gnome=gnomo1
        if dungeon.level == 1:
            gnome=gnomo2
        if dungeon.level == 2:
            gnome=gnomo3

        dungeon.render(player1,gnome)

        #print('-----',player1.loc(),pickaxe.loc(),'------')
        #print(dungeon.are_connected(player1.loc(), pickaxe.loc()))
        
        #posiciones de los jugadores
        position_xy_gnomo=gnome.loc()
        position_xy_human=player1.loc()

        #movimiento y ataques
        key = msvcrt.getch().decode('UTF-8')
        if key=="w":
            position_xy_human=move_up(position_xy_human)
        elif key=="s":
            position_xy_human=move_down(position_xy_human)
        elif key=="d":
            position_xy_human=move_right(position_xy_human)
        elif key=="a":
            position_xy_human=move_left(position_xy_human)

        if is_in_dungeon(position_xy_human) and position_xy_human!=gnome.loc():
            if dungeon.is_walkable(position_xy_human) :
                player1=move_to(player1,position_xy_human)
            elif player1.tool:
                dungeon.dig(position_xy_human)
                player1=move_to(player1,position_xy_human)
        elif is_in_dungeon(position_xy_human) and dungeon.is_walkable(position_xy_human):
            #ataque del jugador al gnomo
            attack(player1, gnome)

        position_xy_human=player1.loc()
        
        position_xy_gnomo=move_gnomo(gnome.loc(),dungeon)

        if position_xy_gnomo!=position_xy_human and gnome.alive:
            gnome.move_to(position_xy_gnomo)

        elif gnome.alive:
            #ataque del gnomo hacia el jugador
            attack(gnome, player1)
    
        #condiciones si el juegador agarra los items
        dungeon.get_items(player1.loc())

        if player1.loc()==pickaxe.loc() and dungeon.level==0:
            player1.tool=True
        
        
        if player1.loc()==sword.loc() and dungeon.level==1:
            player1.has_sword()
        
        if player1.loc()==amulet.loc() and dungeon.level==2:
            player1.treasure=True

        #escaleras
        if dungeon.loc(player1.loc()).face =='<':
            dungeon.level-=1
        elif dungeon.loc(player1.loc()).face =='>':
            dungeon.level+=1


        #si se muere el jugador, termina el juego
        if player1.hp<=0:
            player1.kill()
        if not player1.alive:
            break

        #si se muere el gnomo, le cambiamos el caracter, dejamos el cadaver en el mapa
        if gnome.hp<=0:
            gnome.kill()
            gnome.face='%'
        



            

        
        
        
        
        
        
    if player1.treasure and player1.alive:
        print("You Win!!")
    else:
        print("You Lose..Try again!")
        
        
        

        

        
        
        
        

    # Salió del loop principal, termina el juego
