def esletra(x):
    if x>="a" and x<="z":
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

def encontrar(l,c):
    l=minuscula(l)
    aux=0
    cont=0
    while aux<=len(l)-len(c):
        texto=""
        auxc=0
        if l[aux]==c[auxc]:
            while auxc<len(c):
                texto+=l[aux+auxc]
                auxc+=1
        if texto==c:
            cont+=1
        aux+=1
    return cont

def main():
    l=input("Ingrese texto")
    c=input("Ingrese texto c")
    print(encontrar(l,c))
    


main()