# Ejercicio Calcular el Producto de dos Matrices

# Se define la función para calcular el producto de las dos matrices

def multiplicar_matrices(matriz1, matriz2):
    # Verficar las dimensiones de las matrices
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Las dimensiones de las matrices no son compatibles apra la multiplicación.")
    
    # Matriz resultante con ceros
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    # Realizar la multiplicación de las dos matrices
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

# Ejemplo del resultado del producto de dos matrices

matriz_a = [
    [4, 7, 8],
    [9, 12, 3]
]

matriz_b = [
    [9, 12],
    [14, 15],
    [4, 9]
]

# Funcion para obtener el resultado
resultado = multiplicar_matrices(matriz_a, matriz_b)

# Resultado
for fila in resultado:
    print(fila)