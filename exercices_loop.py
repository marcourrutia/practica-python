import os
os.system("cls")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for num in range(2, 21, 2):
    print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]

aux = 0

for sum in numeros:
    aux += sum

prom = aux / len(numeros)
print(f"\n - El promedio es: {int(prom)}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
aux = numeros[0]

for num in numeros:
    if num > aux:
        aux = num

print(f"El numero mayor es: {aux}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]

new_list = [palabra for palabra in palabras if len(palabra) > 5]

print(f"Nueva lista: {new_list}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input("Ingresa una letra: ").lower()
contador = 0

for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1

print(f"Hay {contador} palabras que empiezan con la letra {letra}")
