from random import randint

print("\nA fierce competition begins between a self-identified human and a self-proclaimed machine.\n\nRock, Paper, Scissors. Best out of 5 wins")

pScore = 0
cScore = 0

# It's the players turn to type in, which gets converted to a number for ease

def playerTurn():
    global pScore

    player = input("\nPress 'r' for ROCK, 'p' for PAPER, 's' for SCISSORS.............")

    if player == "r":
        player = 1
        print("\nYou threw out ROCK")
    elif player == "p":
        player = 2
        print("\nYou threw out PAPER")
    elif player == "s":
        player = 3
        print("\nYou threw out SCISSORS")
    else:
        print("There's something wrong with the player code")

    return player

# Generating the random number

def genRandomNumber():
    randomNumber = randint(1,3)

    return randomNumber

# Creating the computers turn by generating the random number and choosing what to print based on that

def computerTurn():
    randomNumber = genRandomNumber()

    if randomNumber == 1:
        print("\nThe machine threw out ROCK")
    elif randomNumber == 2:
        print("\nThe machine threw out PAPER")
    elif randomNumber == 3:
        print("\nThe machine threw out SCISSORS")
    else:
        print("\nThere's something wrong with your RNG")

    return randomNumber

def winner():
    global cScore
    global pScore

    player = playerTurn()
    computer = computerTurn()

    if player == computer:
        print("\nIt's a DRAW!!")
    elif player == 1 and computer == 3:
        print("\nYour ROCK crushes the SCISSORS. YOU WIN!!")
        pScore += 1
    elif player == 1 and computer == 2:
        print("\nYour ROCK is eclipsed by PAPER, better luck next time.")
        cScore += 1
    elif player == 2 and computer == 1:
        print("\nYour PAPER eclipses the ROCK, YOU WIN!!")
        pScore += 1
    elif player == 2 and computer == 3:
        print("\nYour PAPER was given a vasectomy by the SCISSORS, better luck next time.")
        cScore += 1
    elif player == 3 and computer == 1:
        print("\nYour SCISSORS were crushed by ROCK, better luck next time.")
        cScore += 1
    elif player == 3 and computer == 2:
        print("\nYour SCISSORS gave a vasectomy to the PAPER, YOU WIN!!")
        pScore += 1
    else:
        print("\nThere's something wrong with winner code")

    return pScore, cScore

def main():
    global pScore
    global cScore

    winner()

    print("\n\t\t\t\t\t\t\tSelf-identified Human:", pScore, "\n\t\t\t\t\t\t\tSelf-proclaimed Machine:", cScore)

    if pScore == 3:
        print("YOUUUUUUUUUUUUUUUU WIIIIIIIIIIIIIIN...\n")
    elif cScore == 3:
        print("YOU LOSE...\n")
    else:
        print("\nLet's go again!")
    return

while pScore < 3 and cScore < 3:
    main()
