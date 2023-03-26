notaDesarrolloSoftware = float(input("ingrese nota de desarrollo de software"))
notaMatematicas = float(input("ingrese nota de desarrollo de matemáticas"))
notaLogica = float(input("ingrese nota de desarrollo de lógica de programación"))
promedio = (notaDesarrolloSoftware + notaMatematicas + notaLogica)/3
print(promedio)
if (promedio>=3):
    print("aprobado")
else:
    print("reprobado")


