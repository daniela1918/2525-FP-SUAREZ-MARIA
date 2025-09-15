# Matriz bidimensional 3x3
matriz = [
    [9, 4, 7],
    [3, 8, 1],
    [5, 2, 6]
]

# Función para ordenar una fila con Bubble Sort
def ordenar_fila(matriz, fila_index):
    n = len(matriz[fila_index])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matriz[fila_index][j] > matriz[fila_index][j + 1]:
                # Intercambiar valores
                matriz[fila_index][j], matriz[fila_index][j + 1] = matriz[fila_index][j + 1], matriz[fila_index][j]
    return matriz

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (ejemplo: fila 1, segunda fila)
fila_a_ordenar = 1

# Ordenar la fila
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz después de ordenar la fila
print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz_ordenada:
    print(fila)
