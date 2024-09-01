#Pide al usuario ingresar 7 números y muestra cuál es el mayor de ellos.
print("Ingrese el valor de 7 numeros")
numeros = []

for i in range(7):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

numero_mayor = max(numeros)

print(f"El número mayor de los ingresados es: {numero_mayor}")
