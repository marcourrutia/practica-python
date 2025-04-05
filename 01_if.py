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
