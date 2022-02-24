n = int(input("Digite um número inteiro:"))
verificador = True
i = 30
p = 20
if n < 100:
    i = n % 10
    p = n // 10

    if i == p:
         verificador = False
else:
    while (n // 10) != 0 or verificador:
        p = i
        i = n % 10
        n = n // 10
        if p == i:
            verificador = False
    
if verificador:
    print("não")
else:
    print("sim")

fat
