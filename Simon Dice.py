import random

def simonescucha(secuencia):
    x = 0
    sigue = True
    print("Introduzca valores:")
    while sigue == True and x < len(secuencia):
        print("Pos ", x)
        b = input()
        if (int(secuencia[x]) == int(b)):
            x = x + 1
            sigue = True
        else:
            print("Perdio una vida")
            print("Score: ", len(secuencia) - 1)
            input("Enter para salir")
            sigue = False
    if sigue == False:
        return False
    else:
        return True


def simondice(simon):
    a = random.randint(1, 4)
    print("Valor: ", a)
    simon.append(a)
    return simon

sigue = True
simon = []
while sigue:
    simon = simondice(simon)
    sigue = simonescucha(simon)