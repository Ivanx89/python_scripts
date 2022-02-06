#Realizar división de dos números con control de errores.

x = float(input("Escriba un número: "))


y = float(input("Escriba otro número: "))

if y == 0:
    print("ERROR, el divisor no puede ser cero")
else:
    print(f"{x} entre {y} es {x//y}")