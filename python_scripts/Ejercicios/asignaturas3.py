

# Creamos una lista con las asignaturas:


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = []


for i in asignaturas:
    nota = input(f"Introduce la nota de {i}: ")
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} tienes un {notas[i]}")
