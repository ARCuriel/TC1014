# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ06

import random

op = 5
print("***RANDOM NUMBERS***")
print("Choose a number between 1 - 100, you have", op, "chances")
x = int(input("--Number: "))
y = random.randint(1, 100)

print ("Ssssh, the number is", y)

op = op - 1
while (op>0):
    op = op - 1
    if (x==y):
        print ("You are cheating don't you? Just kidding congratulations!!")
        break
    else:
            if (x>y):
                print("Your number is too high")
                x = int(input(("Try again: ")))
            else:
                print("Your number is too low")
                x = int(input(("Try again: ")))
while (op==0):
    print("No chances left, no problem you can do it better next time :)")
    break
