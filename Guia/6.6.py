import random
def operaciones(n1,n2):
    a=(n1+n2)
    b=n1-n2
    c=n1*n2
    d=n1/n2
    e=a,b,c,d
    if b==(n1-n2):
        return True
    elif a==n1+n2:
        return False

def main():
    n1=int(input("Ingrese numeros"))
    n2=int(input("Ingrese numeros"))
    print(operaciones(n1,n2))
    
main()
    