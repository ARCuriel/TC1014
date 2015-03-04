# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ08

def sum_numbers(x, y):
    return x + y

def difference_numbers(x, y):
    return x - y

def product_numbers(x, y):
    return x * y

def division_numbers(x, y):
    return x // y

def remainder_numbers(x, y):
    return x % y

N1 = int(input("Give me your first number: "))
N2 = int(input("Give me your second number: "))

Sum = sum_numbers(N1, N2)
Diff = difference_numbers(N1, N2)
Prod = product_numbers(N1, N2)
Div = division_numbers(N1, N2)
Rem = remainder_numbers(N1, N2)

print("The sum of your numbers is:", Sum)
print("The difference of your numbers is:", Diff)
print("The product of your numbers is:", Prod)
print("The integrer division of your numbers is:", Div)
print("The remainder of the integrer division of your numbers is:", Rem)
