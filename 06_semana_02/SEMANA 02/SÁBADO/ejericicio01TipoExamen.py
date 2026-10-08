"""
Calculculadora de promedios de notas:
Pide al usuario cuentas notas quiere ingresar. Us aun bucle para solicitar
cada nota, sumarlas y al final mostrar el promedio.
"""
cantidad = int(input("Introduce la cantidad de notas: "))
total = 0
for i in range(cantidad):
    nota = int(input(f"Ingresa la nota {i+1} : "))
    total = total + nota

print(f"El promedio es: {total/cantidad}")