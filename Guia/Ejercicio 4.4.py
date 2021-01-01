def funcion(a):
    x = 1
    y = 0
    while x < a:
        if a % x == 0:
            y = y + x
        x = x + 1
    if y == a:
        return True
    else:
        return False

i = 0
k = 0
while k < 4:
    if funcion(i) == True:
        print (i)
    i = i + 1
k = k + 1

