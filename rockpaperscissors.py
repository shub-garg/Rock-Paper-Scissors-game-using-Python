import random, os, sys
compscore = 0
userscore = 0
numgames = int(input("Welcome to rock, paper, scissors.\nHow many times would you like to play?\n"))
userinput = ""
compchoice = ""
userwin = False
draw = False
choice = ""
clear = lambda: os.system("cls")

for x in range(0, numgames):
    randomno = random.randint(1,3)
    if randomno == 1:
        compchoice = "rock"
    elif randomno == 2:
        compchoice = "paper"
    elif randomno == 3:
        compchoice = "scissors"

    userinput = input("Select rock, paper, or scissors\n")

    if userinput == "rock" and compchoice == "scissors":
        print(userinput,"smashes",compchoice,"You won this round!")
        userscore += 1
    elif userinput == "rock" and compchoice == "paper":
        print(compchoice,"wraps",userinput,"You lost this round!")
        compscore += 1
    if userinput == "paper" and compchoice == "rock":
        print(userinput,"wraps",compchoice,"You won this round!")
        userscore += 1
    elif userinput == "paper" and compchoice == "scissors":
        print(compchoice,"cuts",userinput,". You lost this round!")
        compscore += 1
    if userinput == "scissors" and compchoice == "paper":
        print(userinput,"cuts",compchoice,"You won this round!")
        userscore += 1
    elif userinput == "scissors" and compchoice == "rock":
        print(compchoice,"smashes",userinput,"You lost this round!")
        compscore += 1
    elif (userinput == "rock" and compchoice == "rock") or (userinput == "scissors" and compchoice == "scissors") or (userinput == "paper" and compchoice == "paper"):
        print("Its a Draw!")

if userscore > compscore:
    userwin = True
elif userscore == compscore:
    draw = True

if userwin == True:
    print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",compscore)
elif draw == True:
    print("You drew!\nYour score:",userscore,"\nComputer's score:",compscore)
elif userwin == False:
    print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",compscore)

choice = str(input("Would you like to play again? y/n\n"))
if choice == "y":
    clear()
    os.system("rockpaperscissors.py")
