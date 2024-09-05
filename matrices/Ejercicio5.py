# Solicita una matriz cuadrada de tamaño 3x3 y muestra los elementos de su diagonal principal
matriz = []
print("Por favor, ingrese los valores para la matriz 3x3")

for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"Elemeto [{i + 1}][{j + 1}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nLa matriz ingresada es: ")
for fila in matriz:
    print(fila)

print("\nElementos de la diagonal principal:")
for i in range(3):
    print(matriz[i][i])