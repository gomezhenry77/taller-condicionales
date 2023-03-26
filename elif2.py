color1 = int(input("digite número según elección: \n 1. Amarillo \n 2. Azul \n 3. Rojo \n 4. Blanco \n 5. Negro\n"))
print(color1)
color2 = int(input("digite número según elección: \n 1. Amarillo \n 2. Azul \n 3. Rojo \n 4. Blanco \n 5. Negro\n"))
print(color2)
if (color1 == 1 and color2 == 2):
    print("ha creado el color verde")
elif(color1 == 1 and color2 == 3):
    print("ha creado el color naranja")
elif(color1 == 2 and color2 == 3):
    print("ha creado el color morado")
else:
    print("opción no válida")

