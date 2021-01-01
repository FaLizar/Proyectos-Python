aplazo = 0
aprobado = 0
promocion = 0
nota = int(input("Ingrese la nota: "))
cantidad = 1
while nota != 0:
    if nota < 4:
        aplazo = aplazo + 1
    if nota >= 4 and nota <= 7:
        aprobado = aprobado + 1
    if nota > 7 and nota <= 10:
        promocion = promocion + 1
    nota = int(input("Ingrese la nota: "))
    cantidad = cantidad + 1
porAplazados = ((aplazo / cantidad) * 100)
porAprobados = ((aprobado / cantidad) * 100)
porPromocionados = ((promocion / cantidad) * 100)

print ("Cantidad de aplazos: {} ({}%)".format(aplazo, porAplazados))
print ("Cantidad de aprobados: {} ({}%)".format(aprobado, porAprobados))
print ("Cantidad de promocionados: {} ({}%)".format(promocion, porPromocionados))

