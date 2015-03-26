# Aram Rodrigo Curiel Graxiola
# A01229982
# Quiz 8

def find_threes(x):
    sum = 0
    for element in x:
        if(element%3 == 0):
            sum = sum + element
    return sum

x = [0,4,2,6,9,8,3,12]

do_find = find_threes(x)
print("LIST:",x)
print("The sum from all the elements which are divisible by 3 is:",do_find)
