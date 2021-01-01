cp=1.005
r=2501
ca=1.868
auxomega=0.622

aux=int(input("Ingrese opcion: 1- entalpia 2-omega 3- despejar pv(tengo w)"))

if aux == 1:
    t=int(input("Ingrese t"))
    w=float(input("Ingrese w"))
    entalpia= cp * t +  ( w * (r + (ca*t)))
    print("entalpia: " , entalpia)
elif aux==2:
    w=float(input("Ingrese pv"))
    p=float(input("Ingrese p total"))
    total= auxomega * (w/(p-w))
    print("omega: ",total)
elif aux==3:
    w=float(input("ingrese w"))
    p=float(input("Ingrese p total"))
    total= ((w/auxomega)*p)/((w/auxomega)+1)
    print("pv: ",total)