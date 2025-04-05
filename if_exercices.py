import os
os.system("cls")
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

""" num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
if num1 == num2:
    print("Los números son iguales.")
else:
    print("El número mayor es:", num1 if num1 > num2 else num2)

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operador = input("Que operación deseas hacer?: (+, -, *, /) ")

if operador == "+":
    result = num1 + num2
elif operador == "-":
    result = num1 - num2
elif operador == "*":
    result = num1 * num2
elif operador == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error, división por 0"
else:
    result = "Operador no valido"

print(result) """
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

""" año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto") """

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad: "))

if edad >= 65:
    result = "Adulto Mayor"
elif edad >= 18:
    result = "Adulto"
elif edad >= 13:
    result = "Adolecente"
elif edad >= 3:
    result = "Niño"
elif edad >= 0:
    result = "Bebé"
else:
    result = "Edad no valida"

print(f"Según la edad la clasificación es {result}")
