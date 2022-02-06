#Escribir en un csv datos de otro csv cuya primera columna empiece por VC

import csv

try:

    with open("casos_tecnica_ccaa.csv", "r") as file:
        with open("casos_VC.csv", "w") as escr:
            reader = csv.reader(file)
            for each_row in reader:
                if each_row[0] == "VC":
                    escr.write(', '.join(each_row) + '\n')
except:
    print("ERROR")




