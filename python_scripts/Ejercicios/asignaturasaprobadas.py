#Mostrar asignaturas suspendidas.

asignaturas = ["Matemáticas", "Física", "Química", "Historia"]

aprobadas = []

for i in asignaturas:
    nota = float(input(f"Introduzca la nota de {i}: "))
    if nota >= 5:
        aprobadas.append(i)

for j in aprobadas:
    asignaturas.remove(j)

print(f"Tienes que repetir {asignaturas}")