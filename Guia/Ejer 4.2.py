x = int(input("inrgese un numero"))
maximo = x
minimo = x
while x != 0:
    if x > maximo:
        maximo = x
    if x < minimo:
        minimo = x
    x = int(input("Ingrese un numero:"))
if maximo == 0 and minimo == 0:
    print("no se ingresaron numeros")
else:
    print("el mayor es:", maximo, "el menor es:", minimo)
