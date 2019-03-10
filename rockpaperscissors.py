import random

dict = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
CPUchoices = ("rock", "paper", "scissors")


def checkresult(guess,CPUguess):
    if guess == CPUguess:
        return "Draw!"
    for item in dict:
        if guess == item and CPUguess == dict[item]:
            return "You win!"
    else:
        return "CPU wins!"

def letter2word():
    global guess
    guess = input("type your choice:").lower()
    if guess == "r": guess = "rock"
    elif guess == "p": guess = "paper"
    elif guess == "s": guess = "scissors"
    return guess

while(True):
    print("Let's play. Rock, Paper or Scissors? (r, p, s ?)")
    letter2word()
    while guess not in CPUchoices:
        print("Wrong input, try again!")
        letter2word()
    CPUguess = random.choice(CPUchoices)
    print("you choose: ", guess, "\nand CPU choose: ", CPUguess, "\n")
    print(checkresult(guess,CPUguess))
    again = input("\nPlay again?")
    if again.lower() in ("n", "no"): break



