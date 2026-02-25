#Ejercicios 01: list
areas = ["matematica", "fisica", "quimica"]
areas.append("biologia")
print(areas)

#Ejercicio 02: tupla
coordendas = (10,50) # (X,Y)
#coordendas[0] = 20

#Ejercicio 03: diccionario
estudiantes = {
    "nombre": "Jean",
    "edad":15,
    "notas":[10,20,15]    
}

print(f"Nota más alta: {max(estudiantes['notas'])} ")