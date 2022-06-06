from re import X
import mapping
from human import Human
from gnomo import kobold,knoker,spriggan
import items
from actions import *
import msvcrt

from mapping import Level

ROWS = 25
COLUMNS = 80
def game(name_player1):
    '''
    
    '''
    #Initial parameters
    turns = 0
    #You need that the pickaxe and the human be conected
    while True:
            dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
            pickaxe=items.PickAxe("pickacke",dungeon.find_free_tile())
            player1 = Human(name_player1, dungeon.find_free_tile())
            if dungeon.are_connected(player1.loc(), pickaxe.loc(),[]):
                break
    #Gnomos
    gnomo1 = kobold('Kobold', dungeon.find_free_tile())
    gnomo2 = knoker('Knoker', dungeon.find_free_tile())
    gnomo3 = spriggan('Spriggan', dungeon.find_free_tile())
    #Items
    
    sword=items.Sword("sword",dungeon.find_free_tile())
    amulet=items.Amulet("amulet",dungeon.find_free_tile())

    dungeon.add_item(pickaxe, pickaxe.loc(),1)
    

    while dungeon.level >= 0:
        #Put a gnomo in every dungeon
        gnome=select_gnome(dungeon.level,gnomo1,gnomo2,gnomo3)  
        #If the Gnome dies, it face changes (representing its corpse) and some items will apear.
        gnomo_unlocks(dungeon,gnome,player1,amulet,sword)
        #Game interface
        print('\nLevel:',dungeon.level, str(player1))
        #Render all the game
        dungeon.render(player1,gnome)
        #Game interface
        print(str(gnome))
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
        position_xy_gnomo=move_gnomo(position_xy_gnomo,position_xy_human,dungeon,pickaxe,amulet,sword,[])
        #Gnome´s moves and attacks towards the Player
        gnomo_move_and_attack(player1,gnome,position_xy_human,position_xy_gnomo)
        #Player grabs the items
        pickup(dungeon,player1,pickaxe,sword,amulet)
        #Stairs function
        stairs(dungeon,player1)
        #if the Player dies, the game ends
        if human_is_dead(player1):
            break
        turns += 1
    #Out of the principal loop. The game ends 
    if player1.treasure and player1.alive:
        print("\nYou Win!!")
    else:
        print("\nYou Lose..Try again!")

    
