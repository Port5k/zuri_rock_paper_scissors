# ROCK - PAPER - SCISSORS

from random import choice

name = input("Hi,please input your name: ").title()

options = ['R', 'P', 'S']

def computerPick():
    return choice(options)

def userPick():
    user_pick = (str(input("Pick an option =>\n'R' for Rock\n'P' for Paper\n'S' for Scissors\nYour input: "))).upper()
    if user_pick not in options:
        print("\nInvalid option!\nPlease,try again\n")
        userPick()
    else:
        return user_pick

def result(*options):
    options = list(options)
    for i in range(len(options)):
        if options[i] == 'R':
            options[i] = 'Rock'
        elif options[i] == 'P':
            options[i] = 'Paper'
        elif options[i] == 'S':
            options[i] = 'Scissors'
    print(f"{name}({options[0]}) : CPU({options[1]})")

def gamePlay(userOption, computerOption):
    if userOption == computerOption:
        result(userOption, computerOption)
        print("It's a draw, try again")
        gamePlay(userPick(), computerPick())
    elif userOption == 'R' and computerOption == 'P':
        result(userOption, computerOption)
        print("Computer wins")
    elif userOption == 'R' and computerOption == 'S':
        result(userOption, computerOption)
        print(f"{name} wins")
    elif userOption == 'P' and computerOption == 'R':
        result(userOption, computerOption)
        print(f"{name} wins")
    elif userOption == 'P' and computerOption == 'S':
        result(userOption, computerOption)
        print("Computer wins")
    elif userOption == 'S' and computerOption == 'R':
        result(userOption, computerOption)
        print("Computer wins")
    elif userOption == 'S' and computerOption == 'P':
        result(userOption, computerOption)
        print(f"{name} wins")

gamePlay(userPick(), computerPick())

