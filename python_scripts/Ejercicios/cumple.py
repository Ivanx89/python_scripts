
#NO ESTÁ BIEN HECHO, NO VA
try:
    n = input("Introduce las fechas: ").split()

    dia = list()
    mes = list()
    for i in range(len(n)):
        fecha = n[i].split("/")
        dia.append(0)
        mes.append(1)

    for j in range(1, len(dia)):
        if dia[0] == dia [j] and mes[0] == mes[j]:
            print("SI")
            break
        else:
            print("NO")
            break
    

except ValueError:
    print("Error")
