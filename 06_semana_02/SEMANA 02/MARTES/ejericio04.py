"""
Ejercicio04: Conversor de unidades (pies->metros).
Usando las tuplas (ya qie no deben cambiar).
Pedir al usuario una cantidad en metros y mostrarla en pies. 
"""

# INGRESO
CONVERSION = (0.3048, 0.0254) # (pies, pulgadas)
metros = float(input("Ingrese una cantidad en metros: "))

# PROCESO
pies = metros * CONVERSION[0]
pulgadas = metros * CONVERSION[1]

# SALIDA
print(f"{metros} metros son {pies} pies")
print(f"{metros} metros son {pulgadas} pulgadas")