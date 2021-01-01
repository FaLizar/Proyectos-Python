def agregardicEle(dic):
    n=int(input("Ingrese numero:"))
    while n not in dic and n!=0:
        lst=[]
        lst2=[]
        lst3=[]
        a=input("Ingrese nombre")
        b=input("Ingrese apellido")
        lst2.append(a)
        lst2.append(b)
        c=int(input("Ingrese notas:"))
        lst3.append(c)
        cont=0
        while cont<2:
            c=int(input("Ingrese notas"))
            lst3.append(c)
            cont+=1
        lst.append(lst2)
        lst.append(lst3)
        dic[n]=lst
        n=int(input("Ingrese numero:"))
        while n in dic:
            n=int(input("Numero ya en dic. Ingrese numero:"))
    return dic

def main():
    dic={}
    dic=(agregardicEle(dic))
    print(dic)
    
    
main()
    
