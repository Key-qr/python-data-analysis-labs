"""
while: Se repite mientras una condicion sea verdadera
for: Se usa para iterar sonr euna secuencia
enumerate: Se usa para iterar sobre una secuencia y obtener el indice y el valor
"""

""" Ejercicio 01: Usa el while para imprimir los números del 1 al 10
i = 0
while (i <= 10):
    print(f"{i}")
    i += 1

# Ejercicio 02: Usa el for para imprimir los números del 1 al 10
for i in range(0, 11,2):
    print(f"{i}")


# Ejercicio 03: USa el enumerate para mostrar una lista de compras
# son su numero de posición  
"""
compras = ["Leche", "Pan", "Queso", "Arroz"]

for x, y in enumerate(compras):
    print(f"{x} - {y}")
