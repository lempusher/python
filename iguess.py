#this simple script guesses your number
import random
st = 0
en = 100
gue = 0
print("Please think a numba between 0 and 100 \nI try to guess it. Ready?")
while True:
    numba = random.randint(st, en)
    answer = input(f"Is it {numba}? (y,h,l):")
    gue += 1
    if answer == "h":
        st = numba + 1
    if answer == "l":
        en = numba - 1
    if answer == "y":
        print("I knew it's", numba, "It only took me", gue, "tries.")
        ans2 = input("Play again?")
        if ans2 == "y" or ans2 == "":
            st = 0; en =100
        else: break
