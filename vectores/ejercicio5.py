# Crea un programa que invierta el orden de un vector de 6 elementos.
print("Ingrese el valor de 6 ")
numeros = []

for i in range(6):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

numeros_invertidos = numeros[::-1]

print("Vector original:", numeros)
print("Vector invertido:", numeros_invertidos)
