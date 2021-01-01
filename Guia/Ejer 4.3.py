def funcion(x):
    a = 1
    b = 0
    while a < x:
        if x % a == 0:
            b = b + 1
        a = a + 1
    if b > 1:
        return True
    else:
        return False

y = int(input("Ingrese un num:"))
j = funcion(y)
print(j)