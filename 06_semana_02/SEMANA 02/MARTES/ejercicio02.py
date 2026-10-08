"""
Ejercicio02: Crear un  programa que guarde el nombre de un producto
y su precio en un diccionario.Calcular el precio fianl con un IGV del 18%
y agregarlo como valor del diccionario. 
"""

# INGRESO
producto = {
    "nombre":"Laptop",
    "precio":800
}
igv = 0.18

# PROCESO
producto["preciofinal"] = producto["precio"]*(1+igv)

# SALIDA
print(f"Resumen de compra: {producto["nombre"]}")
print(f"Total a pagar: {producto['preciofinal']}")
