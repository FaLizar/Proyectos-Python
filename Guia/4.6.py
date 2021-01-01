def aBinario(a):
    rta = 0
    pot = 1
    while a > 0:
        n = a % 2
        rta = rta + (n*pot)
        pot = pot * 10
        a = a // 2
    return rta

num = int(input("Ingrese un numero en base 10: "))
binario = aBinario(num)

print ("{} en binario es: {}".format(num, binario))