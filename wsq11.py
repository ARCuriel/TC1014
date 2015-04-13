# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ11

def palyn(x):
 x = str(x)
 x = x[::-1]
 x = int(x)
 return x

x =int(input("Give me the lower value: "))
y =int(input("Give me the upper value: "))

numrange = [] 
lychrel = []

for i in range(y - x+1): 
 numrange.append(x) 
 x = x+1 

palyndromes = 0
nolychrel = 0
candidates = 0

for i in numrange:
 pal = palyn(i)
 if i==pal:
  palyndromes = palyndromes+1
 else: 
  iteracion1 = pal+i
  iteracion2 = palyn(iteracion1)
  for i1 in range(30):
   if iteracion1==iteracion2:
    nolychrel = nolychrel+1
    break 
   else:
    iteracion1 = iteracion1+iteracion2
    iteracion2 = palyn(iteracion1)
    if (i1==29):
     candidates = candidates+1
     lychrel.append(i)

print("THESE ARE YOUR RESULTS: ")
print("There are",palyndromes,"palyndromes")
print("There is/are",nolychrel,"number(s) which is/are no lychrel")
print("There is/are",candidates,"number(s) which is/are a candidate(s) to be lychrel")

if candidates!=0: 
 print("LYCHREL NUMBERS:", lychrel)
