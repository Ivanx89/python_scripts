

# Renta

renta = float(input("¿Cuál es tu renta anual? "))

# Condiciones
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

# Mostrar por pantalla el tipo impositivo
print("El tipo impositivo es del", tipo, "%")