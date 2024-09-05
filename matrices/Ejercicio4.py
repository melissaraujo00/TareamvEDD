# Realiza la multiplicación de dos matrices de 2x2. Solicita los datos para ambas matrices y muestra el resultado.

matriz1 = []
print("\nPor favor, ingrese los valores para la matriz 1 (2x2)")
for i in range(2):
    fila = []
    for j in range(2):
        valor = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
        fila.append(valor)
    matriz1.append(fila)

matriz2 = []
print("\nPor favor, ingrese los valores para la matriz 2 (2x2)")
for i in range(2):
    fila = []
    for j in range(2):
        valor = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
        fila.append(valor)
    matriz2.append(fila)


resultado = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        resultado[i][j] = (matriz1[i][0] * matriz2[0][j] +
                           matriz1[i][1] * matriz2[1][j])

print("\nMatriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nResultado de la multiplicación:")
for fila in resultado:
    print(fila)
