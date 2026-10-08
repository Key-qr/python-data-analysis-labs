"""
Ejercicio01: Pedir al usuario que ingrese una oración. El programa
debe devolver:
1. La oración en mayúsculas.
2. Cuántas palabras tiene la oración.
3. Cual es el último caracter de la oración. 
"""
# INGRESO
oracion = input("Ingrese una oración: ")

# PROCESO
oracionMayuscula = oracion.upper()
oracionPalabras = len(oracion.split())
oracionUltimaLetra = oracion[4]

# SALIDA
print(f"En mayusculas: {oracionMayuscula}")
print(f"Número de palabras: {oracionPalabras}")
print(f"Última letra: {oracionUltimaLetra}")