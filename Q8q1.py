# Ara Rodrigo Curiel Graxiola
# A01229982
# Quiz 8

def triangle(size):
    for x in range (1,size+1,1):
        print("T" * x)
    for x in range (size-1,0,-1):
        print("T" * x)

x = int(input("Give me a number: "))
triangle(x)
