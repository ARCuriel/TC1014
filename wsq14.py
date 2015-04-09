# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ14

def calculate_e(n):
    a = n
    e = (1+1/a)**a
    return float(e)

x = int(input("Number of decimal points of accuracy: "))

num = calculate_e(x)

print("The estimate of the constant e is:",num)
