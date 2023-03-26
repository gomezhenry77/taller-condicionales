primerNumero = int(input("digite primer número\n"))
segundoNumero = int(input("digite segundo número\n"))
tecerNumero = int(input("digite tercer número\n"))
cuartoNumero = int(input("digite cuarto número\n"))
if (primerNumero == segundoNumero and tecerNumero == cuartoNumero and primerNumero == tecerNumero):
    print("todos los números son iguales")
elif (primerNumero != segundoNumero and primerNumero != tecerNumero and primerNumero != cuartoNumero and segundoNumero != tecerNumero and segundoNumero != cuartoNumero and tecerNumero != cuartoNumero):
    print("todos los números son diferentes")
elif (primerNumero == segundoNumero or primerNumero == tecerNumero or primerNumero == cuartoNumero or segundoNumero == tecerNumero or segundoNumero == cuartoNumero or tecerNumero == cuartoNumero):
    print("hay números reptidos")


