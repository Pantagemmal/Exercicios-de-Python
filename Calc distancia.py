from math import sqrt
a = float(input("Primeira entrada: "))
b = float(input("Segunda entrada: "))
c = float(input("Terceira entrada: "))
d = float(input("Quarta entrada: "))
distancia = sqrt( ((a -c)** 2) + ((b - d)**2))
if distancia >= 10:
    print("longe")
else:
    print("perto")


