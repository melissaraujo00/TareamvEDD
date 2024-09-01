#Crea un programa que pida al usuario ingresar 5 números en un vector y luego calcule la suma de todos los elementos

numeros = []
print("Por favor, ingresar 5 numeros")

for i in range(5):
    numero = float (input(f"Numero {i + 1}: "))
    numeros.append(numero)
sumaNumeros = sum(numeros)
print(f"La suma de todos los elementos del vector es: {sumaNumeros}")