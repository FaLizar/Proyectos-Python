def primo(a):
    i = 1
    div = 0
    while i < a:
        if a % i == 0:
            div = div + 1
        i = i + 1
    if div > 1:
        return False
    else:
        return True

valor = int(input("Ingrese un numero entero: "))
print ("El numero {} es primo?".format(valor))

rta = primo(valor)
print (rta)