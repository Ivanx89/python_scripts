import csv

try:

    total = 0
    with open("casos_tecnica_ccaa.csv", "r") as file:
        with open("casos_VC_acum.csv", "w") as acum:
            reader = csv.reader(file)
            for each_row in reader:
                if each_row[0] == "VC":
                    total += int(each_row[2])
                    acum.write(', '.join(each_row) + ', ' + str(total) +'\n')
except:
    print("ERROR")

