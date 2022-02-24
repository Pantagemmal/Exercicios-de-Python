
resultado = 1

def fatorial1():
    fatorial = int(input("Digite o valor de n: "))
    resultado = 1
    if fatorial == 0 :
        print(resultado)
    else:
        while fatorial > 0:
            resultado = fatorial * resultado
            fatorial = fatorial - 1
        print(resultado)

fatorial1()