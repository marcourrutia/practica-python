contador = 0
while contador < 5:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)

contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")
