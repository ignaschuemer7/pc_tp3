import game
def main():
    """
    Stores the game manu.

    Raises
    ------
    ValueError
        Avoid imput errors.
    """
    while True:
        print("\nLet's play roguelike! \nWhat do you want to do?\n1. Play \n2. Quit")
        while True:
            try:
               principal_menu=int(input("Select at most one option > "))
               if principal_menu !=1 and principal_menu !=2:
                   raise ValueError
               break
            except ValueError:
                print("Oops!  This instance doesn´t take letters or numbers outside 1 or 2.  Try again...")
        if principal_menu==1:
            name_player()
        else:
            break
def name_player():
    '''
    It is responsible for prompting the player to enter a name for their playable character.
    
    '''
    while True:
        try:
            name=input("Put your name: ")
            if len(name) > 10:
                raise ValueError
            break
        except ValueError:
            print("Oops! The name you chose is too long. Try a shorter one.")
    game.game(name)
    
if __name__=='__main__':
    main()


