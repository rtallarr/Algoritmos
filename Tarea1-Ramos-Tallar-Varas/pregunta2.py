#lcs
#**Busca la cadena de similitud mas grande
#**usando programacion dinamica guarda los valores en una matriz de dimension 2.
def lcs(X, Y , L):
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

#fpc
#**funcion que recorre la matriz buscando la cadena de similitud mas larga
#**dependiendo de X rellena la lista con - en las partes que no hay similitud
#**Se uso como referencia https://www.youtube.com/watch?v=er7_2ATj-vk&t=1045s&ab_channel=jorgerodriguezc
def fpc(X , Y , L):
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

#creacion matriz
##crea la matriz en la que se guardaran los valores.
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
    L = lcs(X,Y,L)
    return L

def borrar_numero(palabra):
    con = 0
    while con < len(palabra):
        if(palabra[con] == " "):
            con += 1
            palabra = palabra[con:]
            return(palabra)
        con += 1
    return(-1)

contador_casos = 0; definitivo = ""
num_casos = int(input())
definitivo += str(num_casos) + "\n"
while contador_casos < num_casos:
    contador_output = 0
    
    final1 = []
    final2 = []

    substring1 = ""
    substring2 = ""

    palabra1 = input()
    palabra2 = input()

    Y = borrar_numero(palabra1)
    X = borrar_numero(palabra2)

    L1 = creacion_matriz(X,Y)
    h1 = fpc(X,Y,L1)
    h1 = list(reversed(h1))

    L2 = creacion_matriz(Y,X)
    h2 = fpc(Y,X,L2)
    h2 = list(reversed(h2))

    for i in range(len(h1)):
        #print("letra",h1[i])
        if substring1 != "" and h1[i] != "-":
            #print("sub append", substring1)
            final1.append(substring1)
            substring1 = ""
        elif h1[i] != "-":
            substring1 = ""
        else:
            substring1 += X[i]
            #print("1", substring1)
    if substring1 != "":
        final1.append(substring1)

    for i in range(len(h2)):
        #print("letra",h2[i])
        if substring2 != "" and h2[i] != "-":
            #print("sub append", substring2)
            final2.append(substring2)
            substring2 = ""
        elif h2[i] != "-":
            substring2 = ""
        else:
            substring2 += Y[i]
            #print("2", substring2)
    if substring2 != "":
        final2.append(substring2)

    #print("finals", final2, final1)

    if len(final1) > len(final2):
        min = final2
        definitivo += str(len(final1)) + "\n"
    else:
        min = final1
        definitivo += str(len(final2)) + "\n"

    for i in range(len(min)):
        definitivo += final2[i] + " " + final1[i] + "\n"
        #print(final2[i], final1[i])

    for i in range(len(min)):
        del final1[0]
        del final2[0]

    if len(final1) == len(final2):
        pass
    elif min == final2:
        for i in final1:
            definitivo += " " + i + "\n"
            #print(" "+i)
    else:
        for i in final2:
            definitivo += i + "\n"
            #print(i)

    contador_casos += 1
print(definitivo)