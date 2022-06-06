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
            type_player()
        else:
            break
def type_player():
    while True:
        try:
            name=input("Put your name: ")
            if len(name) > 10:
                raise ValueError
            break
        except ValueError:
            print("Oops! The name you chose is too long. Try a shorter one.")

    while True:
        print("\nSelect your Player: \nWhat do you want to do?\n1. Barbarian, '@' \n2. Knight, '𓀝' \n3. Ninja, '🀀'")
        try:
            choose_player=int(input("Select at most one option > "))
            if choose_player !=1 and choose_player !=2 and choose_player !=3:
                raise ValueError
            break
        except ValueError:
            print("Oops!  This instance doesn´t take letters or numbers outside 1 or 2.  Try again...")
        
    game.game(name,choose_player)
    
if __name__=='__main__':
    main()


