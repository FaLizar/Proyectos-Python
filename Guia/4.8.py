def factorial(a):
    if a != 0:
        fac = a
        while a > 1:
            a = a - 1
            fac = fac * (a)
        return fac
    else:
        return 1

num = int(input("Ingrese un numero mayor que 0: "))

while num < 0:
    print ("El numero es menor que cero")
    num = int(input("Ingrese otro numero: "))

resultado = factorial (num)

print ("{}! = {}".format(num, resultado))