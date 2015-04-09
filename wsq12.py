# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ12

a = int(input("Give me the first value: "))
b = int(input("Give me the second value: "))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)

do_gcd = gcd(a,b)
print ("The Greatest Common Divisor between",a,"and",b,"is",do_gcd)
