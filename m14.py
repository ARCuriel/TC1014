def factorial(n):
    x = n
    y = 1
    while (x > 1):
        y = y * x
        x = x - 1
    return y

n = int(input("Give me anumber: "))
do_fac = factorial(n)
print("The factorial is:",do_fac)
