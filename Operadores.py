"""
Aritmeticos: + - * / % **
Comparativos = == != < > <= >=  Devuelven un true o false
Logicos and(y) or(o) not(no)
"""

#Ejercicio 01: Calcular el área de un circulo de radio 5
#Inicio
radio = 5
pi = 3.1416
#Proceso
area = pi * radio ** 2
#Salida
print("El área del circulo es:", area)

#Ejercicio 02: 
edad = 20
es_mayor = edad >= 30
print("¿Es mayor de edad?: ",es_mayor)

#Ejercicio 03: 
tengo_dinero = False
tengo_tiempo = True

puedo_ir_al_cine = (tengo_dinero or tengo_tiempo)

print("Puedo ir al cine?: ",puedo_ir_al_cine)