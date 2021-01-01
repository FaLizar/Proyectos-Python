contador = 0
while contador < 5:
    num = int(input("Ingrese un numero par"))
    if num % 2 == 0:
        contador = contador + 1
        if num % 4 == 0:
            print("El numero es multiplo de 4")
    else:
        print("El numero que ud invoco no es par")

print("Ya ingreso 5 numeros pares")