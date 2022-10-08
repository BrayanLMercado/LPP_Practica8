'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 8: Arreglos Bidimensionales
Archivo De Funciones
Fecha: 14 De Octubre De 2022
'''

'''
Ejercicio 1: Realizar un programa para encontrar el elemento mayor y menor en una
             matriz de 3x3 de números decimales. Contemplar que la matriz ya está 
             inicializada (puede ser definida por el programador o por el usuario).
             Utilizar una función para encontrar el mayor y otra para encontrar
             el menor, las funciones deben retornar el número mayor o menor según sea el caso.
'''
import random

def mayor(matriz):
    mayor=matriz[0][0]
    for x in range(len(matriz)):
        for t in range(len(matriz[x])):
            if matriz[x][t]>mayor:
                mayor=matriz[x][t]
    return mayor

def menor(matriz):
    menor=matriz[0][0]
    for x in range(len(matriz)):
        for t in range(len(matriz[x])):
            if matriz[x][t]<menor:
                menor=matriz[x][t]
    return menor

'''
Ejercicio 2: Realizar un programa que utilice una matriz de 4 renglones y 4 columnas de
             tipo entero e inicialice todos los elementos de dicho arreglo en 0 excepto
             los elementos de la diagonal, los cuales deben inicializarse en 1 
             (utilizando solo ciclos). Al final imprimir la matriz.
'''

def identidad4x4():
    matriz=[]
    for x in range(4):
        matriz.append([])
        for t in range(4):
            if x==t:
                matriz[x].append(1)
            else:
                matriz[x].append(0)
    printMatriz(matriz)

'''
Ejercicio 3: Realizar un programa donde se utilice una matriz de NxM, utilizando una función
             que inicialice la matriz con datos aleatorias N y M son definidas por el usuario.
             Al final imprimir la matriz resultante.
'''

def randomMatrix():
    n=int(input("Número de Renglones: "))
    m=int(input("Número de Columnas: "))
    matriz=[]
    for x in range(n):
        matriz.append([])
        for t in range(m):
            matriz[x].append(random.randint(1,9))
    printMatriz(matriz)

'''
Ejercicio 4: Realizar un programa donde almacenar en una matriz de máximo 10x10 números flotantes
             y obtener el promedio total y el promedio por fila, (máximo 10x10 significa que el
             usuario ingresa el tamaño y este no deberá exceder de 10x10, este dato debe ser validado).
'''

def randomMatrizFloat():
    ren=int(input("Número De Renglones: "))
    col=int(input("Número De Columnas: "))
    while (ren<0 or ren>10) or (col<0 or col>10):
        print("El Tamaño máximo de la matriz es 10x10")
        ren=int(input("Número De Renglones: "))
        col=int(input("Número De Columnas: "))
    matriz=[]
    for x in range(ren):
        matriz.append([])
        for t in range(col):
            print("Posición",'[',x,']','[',t,']',end=" ")
            aleatorio=float(input("Captura Un Número: "))
            matriz[x].append(aleatorio)
    return matriz

def promediosMatriz(matriz):
    sumaTotal=0
    elementosTotales=0
    for x in range(len(matriz)):
        sumaRenglon=0
        elementos=0
        for t in range(len(matriz[x])):
            sumaRenglon+=matriz[x][t]
            elementos+=1
        sumaTotal+=sumaRenglon
        elementosTotales+=elementos
        promedioRenglon=sumaRenglon/elementos
        print("El Promedio Del Renglon",x+1,"Es:",round(promedioRenglon,3))
    promedioMatrix=sumaTotal/elementosTotales
    print("El Promedio De La Matriz Es:",round(promedioMatrix,3))
    
'''
Ejercicio 5: Realiza un programa donde se inicialicen las siguientes matrices en sus respectivas
             variables (EyF) y en una matrizG almacenar la suma de E+F. Al final imprimir
             la matriz G. (Ver imagen).
'''

def sumaMatrices(matrizE,matrizF):
    matrizG=[]
    for x in range(len(matrizE)):
        matrizG.append([])
        for t in range(len(matrizE[x])):
            matrizG[x].append(matrizE[x][t]+matrizF[x][t])

    print("Matriz E")
    printMatriz(matrizE),print()
    print("Matriz F")
    printMatriz(matrizF),print()
    print("Matriz Resultante (E+F)")
    printMatriz(matrizG)


# Funciones Auxiliares
def printMatriz(matriz):
    for x in range(len(matriz)):
        print("[",end=" ")
        for t in range(len(matriz[x])):
            print(matriz[x][t],end=" ")
        print("]")

def menu():
    print("                     Menu")
    print("1) Mayor y Menor De Una Matriz 3x3")
    print("2) Matriz Identidad 4x4 ")
    print("3) Matriz Aleatoria NxM")
    print("4) Promedio Por Fila Y Total De Una Matriz")
    print("5) Suma De Matrices Definidas")
    print()