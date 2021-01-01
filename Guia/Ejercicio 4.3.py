def funcion(a):
    y = 1
    x = 0
    while a > y:
        if a % y == 0:
            x = x + y
        y = y + 1
    if x == a:
        return True
    else:
        return False

j = 0
k = 0
while j <= 4:
    if funcion(k) == True:
        print(k)
    k = k + 1
j = j + 1