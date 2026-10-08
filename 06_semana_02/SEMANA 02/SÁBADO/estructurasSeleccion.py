"""
Seleccion Simple (if)
Seleccion doble (if-else)
Seleccion multiple (if-elif-else)
"""

"""
Ejercicio 1
Pide un nuúmero al usuario y dile si es positivo o negativo.
"""
num = int(input("Introduce un número: "))
if num >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")

"""
Ejercicio 2
Crea un sistema de grados: si la nota es > 90 es "A", > 80 es "B", 
de lo contrario es "C"
"""

nota = int(input("Introduce la nota: "))
if nota > 90:
    print("Grado: A")
elif nota > 80:
    print("Grado B")
else:
    print("Grado C")

"""
Ejercicio 3
Pregunte la edad y si tiene entrada. Si tien e+ 18 imprima "puede entrar"
"""
edad = int(input("Introduce tu edad: "))
tiene_entrada = True

if edad >= 18  and tiene_entrada:
    print("Puede entrar")
else:
    print("No puede entrar")