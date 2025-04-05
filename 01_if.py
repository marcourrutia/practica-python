import os
os.system("cls")

edad = 16
tiene_carnet = True
if edad >= 18:
    print("Eres mayor de edad)")
else:
    print("eres menor")

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIA 🚔!!!")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("A trabajar")

numero = 3
es_el_tres = numero == 4
print("es_el_tres", es_el_tres)

print("\nLa condicion ternaria")
# [código si verdadero] if [condicion] else [codigo si falso]
edad = 17
print("Eres mayor de edad") if edad >= 18 else print("Eres menor de edad")
