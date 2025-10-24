import random

# Genera una palabra de 4 letras al azar
def generar_palabra():
    palabra = ''
    for i in range(4):
        letra = chr(random.randint(97, 122))  # letras minúsculas
        palabra += letra
    return palabra

# Crea una matriz NxN con palabras aleatorias
def generar_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(generar_palabra())
        matriz.append(fila)
    return matriz

# Muestra la matriz en pantalla
def mostrar_matriz(m):
    for fila in m:
        print('  '.join(fila))
    print()

# Verifica si una palabra tiene alguna vocal
def tiene_vocal(palabra):
    for letra in palabra:
        if letra in 'aeiou':
            return True
    return False

# Divide y vencerás: cuenta cuántas palabras tienen vocal
def contar_vocales(matriz):
    n = len(matriz)

    # caso base: matriz 1x1
    if n == 1:
        if tiene_vocal(matriz[0][0]):
            return 1
        else:
            return 0

    # se divide en 4 submatrices
    mitad = n // 2
    sup_izq = [fila[:mitad] for fila in matriz[:mitad]]
    sup_der = [fila[mitad:] for fila in matriz[:mitad]]
    inf_izq = [fila[:mitad] for fila in matriz[mitad:]]
    inf_der = [fila[mitad:] for fila in matriz[mitad:]]

    # llamadas recursivas
    c1 = contar_vocales(sup_izq)
    c2 = contar_vocales(sup_der)
    c3 = contar_vocales(inf_izq)
    c4 = contar_vocales(inf_der)

    # se suman los resultados
    return c1 + c2 + c3 + c4

# Programa principal
print("=== MATRIZ DE PALABRAS ALEATORIAS ===")
n = int(input("Ingrese el tamaño de la matriz (ejemplo 8): "))

matriz = generar_matriz(n)
print(f"\nMatriz generada {n} x {n}:\n")
mostrar_matriz(matriz)

total = contar_vocales(matriz)
print("Cantidad de palabras que tienen al menos una vocal:", total)
