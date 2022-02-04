try:
    peso = int(input("Introduce el peso máximo de la tela de araña: "))
    nelefantes = list(map(int,input().split()))
    acum = 0;
    x = list()
    for i in nelefantes:
        acum += i
        if acum <= peso:
            x.append(i)
        elif acum > peso:
            break
    print(len(x))

except ValueError:
    print("Algún dato no es admitido")

