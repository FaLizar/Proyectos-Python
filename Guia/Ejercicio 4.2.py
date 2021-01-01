x = int(input("Ingrese un numero entero"))
maximo = x
minimo = x
while x != 0:
    if x > maximo:
        maximo = x
    if x < minimo:
        minimo = x
    x = int(input("Ingrese un numero entero:"))
if maximo == 0 and minimo == 0:
    print("No se ingresaron numeros")
print("El maximo es {} y el minimo es {}".format(maximo, minimo))
