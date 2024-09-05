# Solicita al usuario llenar una matriz de 3x3 y calcula la suma de todos sus elementos
matriz = []
print("Por favor, ingrese los valores para la matriz 3x3")

for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"Elemeto [{i + 1}][{j + 1}]: "))
        fila.append(valor)
    matriz.append(fila)
suma = sum(sum(fila) for fila in matriz)

print("\nLa matriz ingresada es: ")
for fila in matriz:
    print(fila)

print(f"La suma de todos los elementos de la matriz es: {suma}")