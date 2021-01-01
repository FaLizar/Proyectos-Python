def invertir (a):
    rta = 0
    while a != 0:
        num = a % 10
        rta = (rta * 10) + num
        a = a // 10
    return rta

def capicua (b):
    if b == invertir (b):
        return True
    else:
        return False


numero = int(input("Ingrese un numero entero positivo: "))

if capicua(numero) == True:
    print ("El numero {}, es capicua".format(numero))
else:
    print ("El numero {}, no es capicua".format(numero))

