n = int(input("Digite o valor de n:"))
i = 2
resto = n % i

if n % i != 0:
    while i < n:
            i = i + 1
    print("primo")
else:
    print("não primo")
    