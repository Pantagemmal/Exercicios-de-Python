n = int(input("Digite um número inteiro:"))
i = 0

if n < 10:
    print(n)
else:
    while n > 10:
        i = i + (n % 10)
        n = n // 10
    print(i + n)