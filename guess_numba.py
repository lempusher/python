import random
numba = random.randint(1, 9)
gcount = 0
correct = 0

while True:
    guess = input("please guess the number:")
    gcount += 1
    if guess == "exit" :
        print(f"you guessed {gcount-1} times of which {correct} were correct")
        break
    elif int(guess) == numba :
        print(f"You are right it's {guess}!")
        correct += 1
        numba = random.randint(1, 9)
    elif int(guess) < numba : print("No, it's higher")
    elif int(guess) > numba : print("No, it's lower")