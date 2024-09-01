# Escribe un programa que cuente cuántos números positivos se ingresan en un vector de 8 elementos
print("Ingrese 8 numeros negativos y positivos:")
numeros = []

for i in range(8):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
positivos = sum(1 for numero in numeros if numero > 0)

print(f"Se ingresaron {positivos} números positivos.")
