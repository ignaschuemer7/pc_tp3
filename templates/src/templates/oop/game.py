from re import X
import mapping
from human import Human
from gnomo import Gnomo
import items
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
    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    turns = 0
    # player
    player1 = Human('player', dungeon.find_free_tile() ,'@',300)
    # gnomos
    gnomo1 = Gnomo('gnomo', dungeon.find_free_tile() ,'G',50)
    gnomo2 = Gnomo('gnomo', dungeon.find_free_tile() ,'Ĝ',100)
    gnomo3 = Gnomo('gnomo', dungeon.find_free_tile() ,'ğ',200)
    #creamos el pico, espada, tesoro
    pickaxe=items.PickAxe("pickacke",dungeon.find_free_tile())
    sword=items.Sword("sword",dungeon.find_free_tile())
    amulet=items.Amulet("amulet",dungeon.find_free_tile())

    dungeon.add_item(pickaxe, pickaxe.loc(),1)
    dungeon.add_item(sword, sword.loc(),2)
    dungeon.add_item(amulet, amulet.loc(),3)
    
    while dungeon.level >= 0:
        '''
        print(len(dungeon.has_items()))
        #si el jugador no mata el ultimo gnomo, no obtendra el tesoro
        if gnomo3.face=='%' and len(dungeon.has_items())<=2:
            dungeon.add_item(amulet, amulet.loc(),3)
        '''
        turns += 1
        #mostrar valores en pantalla
        print('Level:',dungeon.level, str(player1))
        #segun el nivel, cada gnomo
        gnome=select_gnome(dungeon.level,gnomo1,gnomo2,gnomo3)
        #renderizamos el juego
        dungeon.render(player1,gnome)

        '''
        #print(dungeon.are_connected(player1.loc(), pickaxe.loc()))
        '''
        #posiciones de los jugadores
        position_xy_gnomo=gnome.loc()
        position_xy_human=player1.loc()
        #movimiento y ataques
        key = msvcrt.getch().decode('UTF-8')
        #movimiento del jugador a partir del valor de key
        position_xy_human=player_movements(key,position_xy_human)
        #movimiento y ataque del jugador al gnomo
        player_move_and_attack(dungeon,player1,gnome,position_xy_human,position_xy_gnomo)
        #actualizamos posicion
        position_xy_human=player1.loc()
        position_xy_gnomo=move_gnomo(gnome.loc(),dungeon)
        #movimiento y ataque del gnomo al jugador
        gnomo_move_and_attack(player1,gnome,position_xy_human,position_xy_gnomo)
        #condiciones si el jugador agarra los items
        pickup(dungeon,player1,pickaxe,sword,amulet)
        #escaleras
        stairs(dungeon,player1)
        #si se muere el jugador, termina el juego
        if human_is_dead(player1):
            break
        #si se muere el gnomo, le cambiamos el caracter, dejamos el cadaver en el mapa
        if gnomo_is_dead(gnome):
            gnome.face='%'

    # Salió del loop principal, termina el juego
    if player1.treasure and player1.alive:
        print("You Win!!")
    else:
        print("You Lose..Try again!")
   
    
