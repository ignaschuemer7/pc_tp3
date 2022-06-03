from re import X
import mapping
from human import Human
from gnomo import Gnomo
import items
from actions import *
import msvcrt

ROWS = 25
COLUMNS = 80
def game(name):
    #Initial parameters
    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    turns = 0
    #Caracter
    player1 = Human(name, dungeon.find_free_tile() ,'@',500)
    #Gnomos
    gnomo1 = Gnomo('gnomo', dungeon.find_free_tile() ,'G',50)
    gnomo2 = Gnomo('gnomo', dungeon.find_free_tile() ,'Ĝ',100)
    gnomo3 = Gnomo('gnomo', dungeon.find_free_tile() ,'ğ',200)
    #Items
    pickaxe=items.PickAxe("pickacke",dungeon.find_free_tile())
    sword=items.Sword("sword",dungeon.find_free_tile())
    amulet=items.Amulet("amulet",dungeon.find_free_tile())

    dungeon.add_item(pickaxe, pickaxe.loc(),1)
    #dungeon.add_item(sword, sword.loc(),2)
    #dungeon.add_item(amulet, amulet.loc(),3)
    
    while dungeon.level >= 0:
        #Put a gnomo in every dungeon
        gnome=select_gnome(dungeon.level,gnomo1,gnomo2,gnomo3)

        #If the Gnome dies, it face changes (representing its corpse) and the amulet appeard
        if gnomo_is_dead(gnome) and player1.treasure==False and dungeon.level==2:
            gnome.face='%'
            dungeon.add_item(amulet, amulet.loc(),3)
        if gnomo_is_dead(gnome) and player1.weapon==False and dungeon.level==1:
            gnome.face='%'
            dungeon.add_item(sword, sword.loc(),2)
        
        turns += 1
        #Game interface
        print('Level:',dungeon.level, str(player1))
        
        #Render all the game
        dungeon.render(player1,gnome)

        #print(dungeon.are_connected(player1.loc(), pickaxe.loc()))
        
        #posiciones de los jugadores
        position_xy_gnomo=gnome.loc()
        position_xy_human=player1.loc()
        #Movements and attacks (It is not necessary to press the "enter" key every time you have to do an action.)
        key = msvcrt.getch().decode('UTF-8')
        #Player´s movements 
        position_xy_human=player_movements(key,position_xy_human)
        #Player´s moves and attacks towards the Gnome
        player_move_and_attack(dungeon,player1,gnome,position_xy_human,position_xy_gnomo)
        #Position update
        position_xy_human=player1.loc()
        position_xy_gnomo=move_gnomo(gnome.loc(),dungeon,pickaxe,amulet,sword)
        #Gnome´s moves and attacks towards the Player
        gnomo_move_and_attack(player1,gnome,position_xy_human,position_xy_gnomo)
        #Player grabs the items
        pickup(dungeon,player1,pickaxe,sword,amulet)
        #Stairs function
        stairs(dungeon,player1)
        #if the Player dies, the game ends
        if human_is_dead(player1):
            break
        
    #Out of the principal loop. The game ends 
    if player1.treasure and player1.alive:
        print("You Win!!")
    else:
        print("You Lose..Try again!")

    
