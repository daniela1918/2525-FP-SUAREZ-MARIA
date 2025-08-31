# Matriz 3x3
matriz = [
    [6, 4, 7],
    [3, 8, 1],
    [9, 2, 6]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n-1):
        for j in range(n-1-i):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Mostrar
print("Matriz original:")
for fila in matriz:
    print(fila)

# elegir fila a ordenada
fila_ordenar = 1

# Ordenar la fila específica
matriz[fila_ordenar] = bubble_sort(matriz[fila_ordenar])

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila", fila_ordenar, "ordenada:")
for fila in matriz:
    print(fila)
