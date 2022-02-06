#Sin enunciado.

try:
    ncasos = int(input("Introduce el número de casos: "))
    if ncasos < 1:
        print("El número de casos tiene que ser 1 como mínimo")
    else:
        for i in range(0, ncasos):
            S = float(input("Introduce la ubicación de Spiderman (en metros): "))
            A = float(input("Introduce la ubicación de la 1ª bomba (en metros): "))
            B = float(input("Introduce la ubicación de la 2ª bomba (en metros): "))
            BombaA = abs(S - A)
            BombaB = abs(S - B)
            if BombaA > BombaB:
                print("Spiderman debería ir primero a desactivar la 2ª bomba")
            elif BombaA == BombaB:
                print("Las bombas están en la misma posición")
            else:
                print("Spiderman debería ir primero a desactivar la primera bomba")
except ValueError:
    print("Hay algún número no admitido, tienen que estar comprendidos entre 0 y 10000")
