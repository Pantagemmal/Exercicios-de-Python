n = int(input("Digite o valor de n:"))
i = 2
primo = True

def é_primo(x):
    i = 2
    primo = True
    while resto and i < (n-1) :
        if n % i == 0:
            resto = False
        i = i + 1
    return resto


print(é_primo(10))