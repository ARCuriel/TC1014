# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ09

import sys

op = "Yes"
while (op == "Yes"):
    num = input("Give me a number: ")
# vamos a revisar  que entrada es un int mayor igual que cero

    if (num.isdigit() == False):
        print("Are you serious? (Only INTEGERS)")
    else:
        num = int(num)
        factorial = 1
        if num < 0:
            print("Sorry negative numbers are not accepted")
        else:
            if num == 0:
                print("The Factorial of 0 is 1")
            else:
                for i in range(1, num + 1):
                    factorial = factorial * i
                print("The factorial of",num,"is",factorial)
    op = input("Want to try again? (Yes/No): ")
print ("Have a nice day!! :D")
