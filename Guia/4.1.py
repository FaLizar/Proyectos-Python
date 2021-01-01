i = 0
while i < 5:
    b = int(input("Ingrese un numero par: "))
    if b % 2 == 0:
        i = i + 1
        if b % 4 == 0:
            print ("El numero {} es divisible por 4".format(b))


