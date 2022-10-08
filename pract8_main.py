'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 8: Arreglos Bidimensionales
Archivo De Principal
Fecha: 14 De Octubre De 2022
'''

import pract8_func as pf

matrizE=[[25,2,-2],
         [78,-19,12],
         [46,6,33]]

matrizF=[[123,-46,2],
         [-58,142,18],
         [24,-62,-86]]

pf.menu()
opc=int(input("Selecciona Una Opción: "))
while opc<1 or opc>5:
    print("Selecciona Una Opción Valida")
    pf.menu()
    opc=int(input("Selecciona Una Opción: "))
if opc==1:
    print("Matriz Utilizada")
    pf.printMatriz(matrizF)
    print("El Elemento Mayor De La Matriz Es:",pf.mayor(matrizF))
    print("El Elemento Menor De La Matriz Es:",pf.menor(matrizF))
elif opc==2:
    pf.identidad4x4()
elif opc==3:
    pf.randomMatrix()
elif opc==4:
    randomMatrix=pf.randomMatrizFloat()
    print()
    print("Matriz Utilizada")
    pf.printMatriz(randomMatrix)
    pf.promediosMatriz(randomMatrix)
else:
    pf.sumaMatrices(matrizE,matrizF)