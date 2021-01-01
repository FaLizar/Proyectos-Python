def perfecto (a):
    i = 1
    div = 0
    while i < a:
        if a % i == 0:
            div = div + i
        i = i + 1
    if div == a:
        return True
    else:
        return False

j = 0
k = 0
while j < 4:
    if perfecto(k) == True:
        print (k)
        j = j + 1
    k = k + 1

