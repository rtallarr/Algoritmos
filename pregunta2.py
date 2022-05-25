def lcs1(X, Y , L):
    m = len(X)
    n = len(Y)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L

def findPath(X , Y , L):
    m = len(X)
    n = len(Y)
    palabra = ""
    while(n > 0 and m > 0):
        if(X[m-1] == Y[n-1]):
            palabra += X[m-1]
            n= n-1
            m= m-1
        else:
            if(L[m-1][n] >= L[m][n-1]):
                m= m-1
                palabra+="-"
            else:
                n= n-1
    return palabra

def borrado(X,h):
    m = len(h)-1
    n = len(X)-1
    i = 0
    cambiar = ""
    while(m>=0):
        while i <= n:
            if X[i] == h[m]:
                m-=1
                i+=1
            else:
                cambiar += X[i]
                i+=1
    print("palabra a cambiar: ",cambiar)
    return X

def sacar(A,B,linea):  ##A -> string de inicio  ##B--> string final
    "funcion k va a dividir la linea y borrar lo anterior"
    lineaux = ""
    c,flag = 0,0
    if B == "": #Primer caso solo al inicio
        for x in range(len(linea)):
            if linea[x] == A:
                print(lineaux)
                return lineaux
            else:
                lineaux += linea[x]
    elif A == "": #Segundo caso solo al final
        for x in range(len(linea)):
            if linea[x] == B:
                flag =1
            elif flag == 1:
                lineaux += linea[x]
    else:  #Tercer caso al medio
        while c < len(linea):
            """print("aca",A,B)"""
            if linea[c] == A:
                flag=1
            elif linea[c] == B:
                print(lineaux)
                return lineaux
            elif flag == 1:
                lineaux += linea[c]
            c+=1
    print(lineaux)
    return lineaux

def creacion_matriz(X,Y):
    m = len(X)
    n = len(Y)
    L = []
    for i in range(m+1):
        L.append([])
        for j in range(n+1):
            L[i].append(None)
    
    ##llenado de la matriz.
    for i in range(m + 1):
        L[i][0] = 0
    for j in range(n + 1):
        L[0][j] = 0
    L = lcs1(X,Y,L)
    return L




Y = "GGJAB"
X = "GZJZAMB"

"""
Y = "Este es un texto"
X = "Este es otro texto"
"""
"""
Y = "ABCLGH"
X = "AELFHR"
"""
"""
m = len(X)
n = len(Y)
L = []
for i in range(m+1):
    L.append([])
    for j in range(n+1):
        L[i].append(None)
    
##llenado de la matriz.
for i in range(m + 1):
    L[i][0] = 0
for j in range(n + 1):
    L[0][j] = 0
L = lcs1(X,Y,L)
"""

"""
#para ver la matriz
for i in range(m+1):
    print(L[i])
"""
L1 = creacion_matriz(X,Y)
h1 = findPath(X,Y,L1)
h1 = list(reversed(h1))
print(h1)

L2 = creacion_matriz(Y,X)
h2 = findPath(Y,X,L2)
h2 = list(reversed(h2))
print(h2)
##Falta revisar el primero e ir borrando
for i in range(len(h1)+1):
    #print(i)
    if(h1[i-1] == "-"):
        print(X[i-1])




"""
c = 0
print(h)
while c <= len(h)-1:
    if c == 0:
        sacar(h[0],"",X)
        sacar(h[0],"",Y)
    if c == len(h)-1:
        sacar("",h[c],X)
        sacar("",h[c],Y)
    else:
        sacar(h[c],h[c+1],X)
        sacar(h[c],h[c+1],Y)
    c+=1
"sacar("",h[2],X)"
"borrado(X,h)"
"""