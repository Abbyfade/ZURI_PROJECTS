import random
# r for rock, p for paper, s for scissors
options = ["R", "P", "S"]
print("Welcome to the Rock, Paper, Scissors game!")
user = input("Enter your name: ")

check = input("Enter yes to play or quit to end the game: ").lower()

while check == "yes":
    UserSelection = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()

    if UserSelection not in options:
        print("You didn't enter any of the options given")
        check = input("Enter yes to play or quit to end the game: ").lower()

    else:
        print("computer picks {}".format(options[s].title()))
        if random.choice(options) == UserSelection:
            print("It's a tie")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif random.choice(options)  == "R" and UserSelection == "S":
            print("Computer wins!")
            print("Rock smashes Scissors")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif random.choice(options)  == "R" and UserSelection == "P":
            print("You win!")
            print("Paper covers Rock")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif random.choice(options) == "P" and UserSelection == "R":
            print("Computer wins!")
            print("Paper covers Rock")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif random.choice(options) == "P" and UserSelection == "S":
            print("You win!")
            print("Scissors cuts Paper")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif random.choice(options) == "S" and UserSelection == "R":
            print("You win!")
            print("Rock smashes Scissors")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif random.choice(options)  == "S" and UserSelection == "P":
            print("Computer wins!")
            print("Scissors cuts Paper")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()
