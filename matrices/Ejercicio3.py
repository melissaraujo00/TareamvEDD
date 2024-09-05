# Pide al usuario llenar una matriz de 2x3 y muestra su transpuesta
matriz = []
print("\nPor favor, ingrese los valores para la matriz 3x3")

for i in range(2):
    fila = []
    for j in range(3):
        valor = float(input(f"Elemeto [{i + 1}][{j + 1}]: "))
        fila.append(valor)
    matriz.append(fila)
transpuesta = [[matriz[j][i] for j in range(2)] for i in range(3)]

print("\nLa matriz ingresada es: ")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)

