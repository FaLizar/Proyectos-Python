nota = float(input("Ingrese la nota: "))
aplazados = 0
aprobados = 0
promociona = 0
cantidad = 1
while nota > 0 and nota < 10:
    if nota < 4:
        aplazados = aplazados + 1
    if nota >=4 and nota <= 7:
        aprobados = aprobados + 1
    if nota > 7:
        promociona = promociona + 1
    nota = float(input("Ingrese la nota: "))
    cantidad = cantidad + 1
porcentaje1 = (aplazados / cantidad) * 100
porcentaje2 = (aprobados / cantidad) * 100
porcentaje3 = (promociona / cantidad) * 100
print(porcentaje1, porcentaje2, porcentaje3)