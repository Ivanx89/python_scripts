
edad = int(input("Indique su edad: "))

ingresos = float(input("Indique sus ingresos mensuales: "))

if edad >= 16 and ingresos > 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")