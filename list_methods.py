import os
os.system("cls")

lista1 = ['a', 'b', 'c', 'd']

print(lista1)

###
# METODOS PARA INSERTAR
###

# Inserta un elemento al final de la lista
lista1.append('e')
print(lista1)

# Inserta un elemento en la posición que le indicamos como primer argumento
lista1.insert(1, '@')
print(lista1)

# Inserta más de 1 elemento al final de la lista
lista1.extend(['😊', '😂'])
print(lista1)

###
# METODOS PARA ELIMINAR
###

# Eliminar la primera aparición del elemento que se pasa cómo argumento
lista1.remove('@')
print(lista1)

# Elimina el ultimo elemento de la lista y además lo devuelve. Además se le puede pasar cómo parametro el indice del elemento que se quiere eliminar
ultimo = lista1.pop()
print(ultimo)
print(lista1)

# Eliminar
del lista1[-2]
print(lista1)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
del lista2[2:5]
print("lista 2: ", lista2)

# Eliminar todos los elementos de la lista
lista1.clear()
print(lista1)

###
# OTROS METODOS UTILES
###

# Ordena la lista modificando la original (no devuelve nada)
numbers = [3, 9, 99, 50, 78, 12]
numbers.sort()
print(numbers)

# Ordena la lista creando una copia que se puede guardar en otra variable
numbers2 = [5, 6, 1500, 42, 450, 12, 74, 9]
sorted_numbers = sorted(numbers2)
print("sin ordenar: ", numbers2)
print("Ordenada:    ", sorted_numbers)

# Ordenar lista de cadenas de texto. Pone primero mayusculas a menos que le pase cómo argumento el key
frutas = ['manzana', 'Pera', 'Limon', 'Banana']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

# Se le pasa el key como argumento y compara todo en minúsculas
frutas.sort(key=str.lower)
print("ordenadas con sort", frutas)

# Contar cuantas veces aparece un elemento en la lista
words = ['b', 'c', 'd', 'e', 'f', 'c', 'c']
print("Cuantas 'C'", words.count('c'))

# Comprobar si hay un elemento X en la lista
print('e' in words)
