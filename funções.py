fat = 1
def fatorial(x):
    fat = 1
    if x == 0 :
        fat = 1
    else:
        while x > 0:
            fat = fat * (x)
            x = x - 1
    return fat
        
def fatorial_binomial(x,y):
    return fatorial(x) / (fatorial(y) * (fatorial(x - y)))

print(fatorial_binomial(5,4))