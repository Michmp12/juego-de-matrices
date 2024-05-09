matriz1 = [['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎'],['♡︎','♡︎','♡︎','♡︎','♡︎']]
import os
correcto = '😋'
incorrecto = '💀'
list_pregunta = ['¿Qué es Python?''\n\n1. Juego\n2. Lenguaje de programacion\n4. Marca de auto\n5. Ninguna de las anteriores','¿Que es HTML?\n1. Marca de Computadores\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente\n5.¿Apple es una marcá de?\n\n1. comidas\n2. fruta\n3. colores\n4.celulares\n5.Todas las anteriores']
list_respuesta = ['2','1','4']
def fnt_pintarmatriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end = '    ')
        print('\n')

sw = True
contador = 0
    
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        import os
        os.system('cls')
        fnt_pintarmatriz()
        print()
        print(list_pregunta[contador])
        print()
        respuesta = input('->')
        if respuesta == list_respuesta[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1
        
    