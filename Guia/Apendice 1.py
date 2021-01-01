def valido():
    b = int(input("Ingrese la base: "))
    while b % 2 == 0:
        print("El numero no es valido, ingrese otro")
        b = int(input("Ingrese la base: "))
    return(b)

n = valido()
c = n
f = (n + 1) // 2
for f in range(0, (n + 1) // 2):
    for c in range(0, n):
        if ((f + c) >= n // 2 and (c - f) <= (n // 2)):
            print("x",end="")
        else:
            print(" ",end="")
    print("")
