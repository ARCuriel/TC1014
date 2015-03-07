# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ10

import statistics

def total(num):
    answer = 0
    size = len(num)
    for indice in range(size):
        answer = answer + num[indice]
    return answer

def average(num):
    answer = 0
    size = len(num)
    for indice in range(size):
        answer = answer + num[indice]/size
    return answer

def stand_dev(num):
    answer = statistics.stdev(num)
    return answer 

# main program 
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
n3 = float(input("Third number: "))
n4 = float(input("Fourth number: "))
n5 = float(input("Fifth number: "))
n6 = float(input("Sixth number: "))
n7 = float(input("Seventh number: "))
n8 = float(input("Eighth number: "))
n9 = float(input("Nineth number: "))
n10 = float(input("Tenth number: "))

num = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
print("YOUR LIST =",num)

T = total(num)
A = average(num)
S = stand_dev(num)

print("The Total is",T)
print("The Average of your list is",A)
print("The Standard Deviation of your list is",S)



