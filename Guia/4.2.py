def positivo():
    num = int(input("Ingrese un entero positivo: "))
    while num < 0:
        num = int(input("El numero tiene que ser positivo, ingresa otro: "))
    return num


a = positivo()
maxi = a
mini = a

if a == 0:
    print ("No se ingresaron numeros")

b = 1
while b != 0:
    if b < mini:
        mini = b
    if b > maxi:
        maxi = b
    b = positivo()

print ("El maximo es: {}, el minimo es: {}".format(maxi, mini))


