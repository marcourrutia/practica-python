import os
os.system("cls")

# Iterar una lista
print("Iterar lista")
frutas = ['Manzana', 'Pera', 'Melon', 'Sandía']
for fruta in frutas:
    print(fruta)

# Iterar cadena de texto
print("\nIterar cadena de texto:")
texto = "Marco Urrutia"
for caracter in texto:
    print(caracter)

# enumerate()
print("\n Enumerate:")
nombres = ['Marco', 'Carlos', 'Amanda', 'Carolina', 'Gato Plomo']
for index, nombre in enumerate(nombres):
    print(f"El indice de {nombre} es {index}")

# Bucles anidados
print("\nBucles anidados:")
letras = ['a', 'b', 'c', 'd']
numeros = [1, 2, 3, 4]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")