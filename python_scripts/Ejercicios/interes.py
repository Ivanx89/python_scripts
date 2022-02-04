
#Capital con intereses

try:
    cantidad = float(input("Introduzca cantidad a invertir: "))
except ValueError:
    print("No ha introducido ninguna cantidad")

try:    
    interes = float(input("Introduzca el interés anual: "))
except ValueError:
    print("No ha introducido ningún tipo de interés válido")

try:
    años = int(input("Introduzca el número de años: "))
except:
    print("No ha escrito ningún número")



for i in range(años):
    cantidad *= 1 + interes / 100 
    print("El capital del " + str(i+1) + "º " + "año es: " + str(round(cantidad, 2)) + "€")
