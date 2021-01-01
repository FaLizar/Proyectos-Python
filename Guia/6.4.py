import random

def main():
    lst=[]
    x=int(input("Ingrese numeros lista"))
    while x!=0:
        lst.append(x)
        x=int(input("Ingrese numeros lista"))
    print(lst)
    y=int(input("Ingrese intervalos"))
    z=int(input("Ingrese intervalos"))
    print(funcion(lst,y,z))

def funcion(lst,a,b):
    aux=0
    while aux<len(lst):
        if lst[aux]<a or lst[aux]>b:
            lst[aux]=random.randint(a,b)
        aux+=1
    return lst

main()
    