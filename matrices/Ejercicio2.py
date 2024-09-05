# Genera una matriz identidad de tamaño 4x4
matriz = []
print("\nPor favor, ingrese los valores para la matriz 3x3")

for i in range(4):
    fila = []
    for j in range(4):
        valor = float(input(f"Elemeto [{i + 1}][{j + 1}]: "))
        fila.append(valor)
    matriz.append(fila)
suma = sum(sum(fila) for fila in matriz)

print("\nLa matriz ingresada es: ")
for fila in matriz:
    print(fila)

print(f"\nLa suma de todos los elementos de la matriz es: {suma}")