from game import game
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
                print("\nOops!  This instance doesn´t take letters or numbers outside 1 or 2.  Try again...")
        if principal_menu==1:
            type_player()
        else:
            break

def type_player():
    '''
    Allows the player to choose a name and a character type.

    Raises
    ------
    ValueError
        Avoid imput errors.

    '''
    while True:
        try:
            name=input("\nPut your name: ")
            if len(name) > 10:
                raise ValueError
            break
        except ValueError:
            print("\nOops! The name you chose is too long. Try a shorter one.")

    while True:
        print("\nSelect a character: \n1. Barbarian, '@' \n2. Knight, '𓀝' \n3. Ninja, '🀀' \n4. Characters Description")
        try:
            choose_player=int(input("Select at most one option > "))
            if choose_player !=1 and choose_player !=2 and choose_player !=3 and choose_player !=4:
                raise ValueError
            if choose_player == 4:
                print('\n-Description- \nBarbarian | HP: High | Damage: Low \nKnight | HP: Medium | Damage: Medium \nNinja | HP: Low | Damage: High')
                continue
            break
        except ValueError:
            print("\nOops!  This instance doesn´t take letters or numbers outside 1,2,3 or 4.  Try again...")
    game(name,choose_player)
    
if __name__=='__main__':
    main()


