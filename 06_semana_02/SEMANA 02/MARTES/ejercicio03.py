"""
Ejercicio03: Crear una lista llamada invitados. Pida al usuario un 
nombre para decirle si esta en la listo o no. 
"""
# INGRESO
invitados = ["Juan", "Pedro", "Maria", "Luis"]
nombre = input("¿Cuál es su nombre? ")

# PROCESO
if nombre in invitados:
    mensaje = f"bienvenido {nombre} estas en la lista"
else:
    mensaje = "Lo siento, no estas invitado"

# SALIDA

print(mensaje)