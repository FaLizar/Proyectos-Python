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

def palabra(l,c):
    aux=0
    ayuda=0
    while aux<len(l):
        bandera=0
        palabra=""
        while aux<len(l) and bandera==0:
            if esletra(l[aux])==True:
                palabra+=l[aux]
            else:
                bandera=1
            aux+=1
        print(palabra)
        if funcion(palabra,c)==True:
            ayuda+=1
    if ayuda>0:
        print("Se cumple la condicion")
    else:
        print("No se cumple la condicion")
        
def funcion(l,c):
    if len(l)==len(c):
        contador1=0
        for letra in l:
            for corta in c:
                if corta==letra:
                    contador1+=1
        if contador1==len(l):
            return True
    else:
        return False
    
def main():
    l=input("Ingrese texto")
    c=input("Ingrese corta")
    palabra(l,c)
main()