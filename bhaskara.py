from math import sqrt
a = float(input("Quel est le a?"))
b = float(input("Quel est le b?"))
c = float(input("Quel est le c?"))
R = (b ** 2) - (4*a*c)

if R < 0 :
    print("esta equação não possui raízes reais")
else:
    if R == 0 :
        r1 = (-b) / (2* a)
        print("a raiz desta equação é ", r1)
    else:
        r1 = (-b + sqrt(R)) / (2* a)
        r2 = (-b - sqrt(R)) / (2* a)
        print("as raízes da equação são", r2, "e", r1)


