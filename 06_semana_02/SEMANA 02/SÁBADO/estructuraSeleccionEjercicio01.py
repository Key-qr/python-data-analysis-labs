# Ingreso
unidades = int(input("Introduce las unidades: "))
# Proceso
    # Calculando el importe de compra
    # unidades >= 1 and unidades <= 25  
if 1 <= unidades <= 25:
    impcom = unidades * 27.7
elif 26 <= unidades <= 50:
    impcom = unidades * 25.5
elif 51 <= unidades <= 75:
    impcom = unidades * 23.5
elif unidades >= 76:
    impcom = unidades * 21.5

    # Calculando el importe descuento
if unidades > 50:
    impdes = impcom * 0.15
else:
    impdes = impcom * 0.05
    # Calculando el importe a pagar
imppag = impcom - impdes

# Salida
print(f"El importe de compra es: {impcom:.2f}")
print(f"El importe de descuento es: {impdes:.2f}")
print(f"El importe a pagar es: {imppag:.2f}")