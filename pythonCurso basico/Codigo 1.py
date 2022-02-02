notas = {"Pedro":9.0, "Maria":8.9, "Mateo":8.0, "Paola":8.1}

for nombre, nota in notas.items():
    print("{} obtuvo {}".format(nombre, nota))
grupal = 0
for nota in notas.values():
    grupal += nota
print("El promedio del grupo es:", grupal / len(notas))
print("Alumnos:")
for nombre in notas.keys():
    print("-",nombre)