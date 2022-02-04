g = open("prova2.txt", 'w')
try:
    f = open("prova1.txt", 'r')
except FileNotFoundError:
    print("No existe el fichero")
else:
    for l in f:
        g.write(l)
    f.close()
g.close()