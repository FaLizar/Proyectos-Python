def condicion(a):
    n4 = a // 1000
    n3 = (a % 1000) // 100
    n2 = ((a % 1000) % 100) // 10
    n1 = (((a % 1000) % 100) % 10)
    sumapar = n2 + n4
    sumaimpar = n1 + n3
    if sumapar == sumaimpar:
        return True
    else:
        return False

k = 1000
while k < 10000:
    if condicion(k) == True:
        print (k)
    k = k + 1



