import random


myGold = 0
roundNumber = 0

def move_player (lend_game):
    rewardFromTheBox = ["zielona", "pomarańczowa", "purpurowa", "złota"]

    myGold = 0

    for x in range(lend_game):
        move = random.choices(rewardFromTheBox, [75, 20, 4, 1], k = 1)



        if move == ['zielona']:
            myGold = myGold + 1000
        elif move == ['pomarańczowa']:
            myGold = myGold + 4000
        elif move == ['purpurowa']:
            myGold = myGold + 9000
        elif move == ['złota']:
            myGold = myGold + 16000

        print(move)
    print(myGold)

    return myGold



while True:

    print(
    """ 
        1. Nowa Gra
        2. Najlepszy wynik
        3. Zakończ grę
    """
          )

    menuChoice = int(input("Grasz? :D  "))
    if menuChoice == 1:

        myGold = move_player(5)
        print("Runda: ", roundNumber, "Wynik: ", myGold)

    elif menuChoice == 2:
        print("najlepszy wynik")

    elif menuChoice == 3:
        break
    else:
        print("Dokonona zły wybór, spróbuj jeszcze raz.. ;)")

