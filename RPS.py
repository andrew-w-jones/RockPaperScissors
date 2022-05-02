#!bin/python3
from random import seed
from random import randint
from os import system

playing = True
compwins = 0
playerwins = 0


def c():
    print('\n')


while playing:
    print("Choose a game: \n1. Dice\n2. Coin flip\n3. Rock Paper Scissors\n4. Exit")
    choice = input("\nChoice: ")
    c()
    if choice == '1':
        choiced=0
        while choiced==0:
            choiced = int(input("1 or 2 dice? "))
            if choiced == 1:
                print("")
            if choiced == 2:
                print("")
            elif choiced!= 1 and 2:
                choiced=0
                print("\nSeriously?")
        c()
        if choiced == 1:
            throw = input("Throw? y or n ")
            if throw == "y":
                playdice1again = "y"
                while playdice1again == "y":
                    comp1 = randint(1, 6)
                    player1 = randint(1, 6)
                    print("\nYour throw was " + str(player1))
                    print("My throw was " + str(comp1))
                    if comp1 > player1:
                        print("I win!!!")
                        compwins += 1
                    if comp1 == player1:
                        print("It was a tie.")
                    if player1 > comp1:
                        print("You got me that time...")
                        playerwins += 1
                    print("\nComputer wins: " + str(compwins) + "\nPlayer wins: " + str(playerwins))
                    playdice1again = input("\nRoll again? y or n ")
        if choiced == 2:
            throw = input("Roll? y or n ")
            if throw == "y":
                playdice2again = "y"
                while playdice2again == "y":
                    D2player1 = randint(1, 6)
                    D2comp1 = randint(1, 6)
                    D2comp2 = randint(1, 6)
                    D2player2 = randint(1, 6)
                    c()
                    print("\nYour first roll: " + str(D2player1) + "\nYour second roll: " + str(
                        D2player2) + "\nTotal: " + str(D2player2 + D2player1))
                    print("\nMy first roll: " + str(D2comp1) + "\nMy second roll: " + str(D2comp2) + "\nTotal: " + str(
                        D2comp2 + D2comp1))
                    if D2comp2 + D2comp1 > D2player2 + D2player1:
                        print("I win!!!")
                        compwins += 1
                    if D2comp2 + D2comp1 == D2player2 + D2player1:
                        print("It was a tie.")
                    if D2player1 + D2player2 > D2comp1 + D2comp2:
                        print("You got me that time...")
                        playerwins += 1
                    print("\nComputer wins: " + str(compwins) + "\nPlayer wins: " + str(playerwins))
                    playdice2again = input("\nRoll again? y or n ")
    if choice == '2':
        playcagain = "y"
        while playcagain == "y":
            choicec = input("\nHeads or Tails? (h/t) ")
            c()
            if choicec == "h":
                choicec = 0
            if choicec == "t":
                choicec = 1
            if choicec == 0 or 1:
                coin = ["Heads", "Tails"]
                coinflipint = randint(0, 1)
                coinflip = coin[coinflipint]
                print("\nIt landed on " + coinflip)
                if coinflipint == choicec:
                    print("You win!")
                    playerwins += 1
                if coinflipint != choicec:
                    print("You lost.")
                    compwins += 1
                print("\nComputer wins: " + str(compwins) + "\nPlayer wins: " + str(playerwins))
                playcagain = input("\n Flip again? y or n ")
                playcagainint=0
                if playcagain=="y":
                    playcagainint=1
                if playcagain=="n":
                    playcagainint=1
                while playcagainint==0:
                    playcagain = input("\n Flip again? y or n ")
                    if playcagain == "y":
                        playcagainint = 1
                    if playcagain == "n":
                        playcagainint = 1
    if choice == '3':
        playrpsagain = 'y'
        while playrpsagain == 'y':
            c()
            choicerps = input("Rock, Paper, or Scissors? (r/p/s) ")
            c()
            if choicerps == 'r':
                choicerps = 1
            if choicerps == 'p':
                choicerps = 2
            if choicerps == 's':
                choicerps = 3
            if choicerps != 0:
                rps = ['nothing', 'Rock', 'Paper', 'Scissors']
                comprpschoice = randint(1, 3)
                print("You chose "+rps[choicerps] + "\nI chose " + rps[comprpschoice])
                if comprpschoice == choicerps:
                    print("\nTie!")
                if comprpschoice == 1 and choicerps == 3:
                    print("\nI win!")
                    compwins += 1
                if comprpschoice == 1 and choicerps == 2:
                    print("\nYou win...")
                    playerwins += 1
                if comprpschoice == 2 and choicerps == 3:
                    print("\nYou win...")
                    playerwins += 1
                if comprpschoice == 3 and choicerps == 1:
                    print("\nYou win...")
                    playerwins += 1
                if comprpschoice == 2 and choicerps == 1:
                    print("\nI win!")
                    compwins += 1
                if comprpschoice == 3 and choicerps == 2:
                    print("\nI win!")
                    compwins += 1
                print("\nComputer wins: " + str(compwins) + "\nPlayer wins: " + str(playerwins))
                playrpsagain = input("Play again? y or n ")
    print("\n\n")
    if choice == '4':
	Playing = False
	