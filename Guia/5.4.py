def esletra(x):
    if x>="a" and x<="z":
        return True
    else:
        return False
    
def inicio(t):
    bandera=0
    aux=0
    while aux<len(t) and bandera==0:
        if esletra(t[aux])==True:
            bandera=1
        else:
            aux+=1
    return aux

def fin(t):
    bandera=0
    aux=len(t)-1
    while aux>=0 and bandera==0:
        if esletra(t[aux])==True:
            bandera=1
        else:
            aux-=1
    return aux

def PrincipioFin(t):
    t=minuscula(t)
    auxf=fin(t)
    auxi=inicio(t)
    recorrer=0
    palabrai=""
    palabraf=""
    while recorrer==0:
        bandera=0
        while bandera==0:
            if esletra(t[auxi])==True:
                palabrai+=t[auxi]
            else:
                bandera=1
            auxi+=1
        bandera2=0
        while bandera2==0:
            if esletra(t[auxf])==True:
                palabraf+=t[auxf]
            else:
                bandera2=1
            auxf-=1
        recorrer=1
    print(palabrai,"     ",palabraf[::-1])
    if palabrai==(palabraf[::-1]):
        return True
    else:
        return False

def minuscula(t):
    texto=""
    aux=0
    while aux<len(t):
        if t[aux]>="A" and t[aux]<="Z":
            texto+=chr(ord(t[aux])+32)
        else:
            texto+=t[aux]
        aux+=1
    return texto

    
def main():
    t=input("Ingrese texto")
    print(PrincipioFin(t))
    
main()