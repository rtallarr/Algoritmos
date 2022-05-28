
def lista(lista):#Funcion que lee una lista y guarda una matriz
    matrizaux=list()
    matrizaux2=list()
    matriz=list()
    agua=list()
    for linea in lista:
        if "L" in linea:
            matrizaux.append(linea.split())
        elif "W" in linea:
            matrizaux.append(linea.split())
        elif " " in linea:
            agua.append(linea.split())
    for i in matrizaux:
        matrizaux2=list()
        for j in i:
            for letra in j:
                matrizaux2.append(letra)
        matriz.append(matrizaux2)
    return [matriz,agua]


def recursion(n,m,matriz):
    lista=matriz
    if matriz[n][m]=="L":
        return 0
    elif matriz[n][m]=="W":
        area=1
        lista[n][m]="L"
        if n==0:
            area+=recursion(n+1,m,lista)+recursion(n,m+1,lista)+recursion(n,m-1,lista)+recursion(n+1,m+1,lista)+recursion(n+1,m-1,lista)
        elif m==0:
            area+=recursion(n+1,m,lista)+recursion(n,m+1,lista)+recursion(n+1,m+1,lista)+recursion(n-1,m+1,lista)+recursion(n-1,m,lista)
        elif m==len(lista[n])-1:
            area+=recursion(n+1,m,lista)+recursion(n,m-1,lista)+recursion(n+1,m-1,lista)+recursion(n-1,m-1,lista)+recursion(n-1,m,lista)
        elif n==len(lista)-1:
            area+=recursion(n-1,m,lista)+recursion(n,m+1,lista)+recursion(n-1,m+1,lista)+recursion(n-1,m-1,lista)+recursion(n,m-1,lista)
        else:
            area+=recursion(n-1,m,lista)+recursion(n+1,m,lista)+recursion(n,m-1,lista)+recursion(n,m+1,lista)+recursion(n-1,m-1,lista)+recursion(n-1,m+1,lista)+recursion(n+1,m-1,lista)+recursion(n+1,m+1,lista)
    return area


def archivo2(a):
    archivo=open(a,"r+").read().splitlines()
    dict={}
    c=0
    i=0
    while c < int(archivo[0]):
        dict[c]=list()
        while i < int(len(archivo))-2:
            if '' == archivo[i+2]:
                del archivo[i+2]
                break
            dict[c].append(archivo[i+2])
            del archivo[i+2]
        c+=1
    return dict

def archivo3(diccionario):
    i=0
    while i < len(diccionario):
        diccionario[i]=lista(diccionario[i])
        i+=1
    return diccionario


for i in archivo3(archivo2("ejemplo.txt")):
    for n,m in archivo3(archivo2("ejemplo.txt"))[i][1]:
        print(recursion(int(n)-1,int(m)-1,archivo3(archivo2("ejemplo.txt"))[i][0]))
    print(" ")