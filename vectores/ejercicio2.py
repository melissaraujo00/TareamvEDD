# Solicita 10 números y calcula el promedio de los valores ingresados
print("Ingrese el valor de 10 numeros")
numeros = []

for i in range(10):
    numero = int(input(f"Numero {i + 1}: "))
    numeros.append(numero)
promedio = sum(numeros)/ len(numeros)

print(f"El promedio de los numeros ingresado es: {promedio:.2f}")