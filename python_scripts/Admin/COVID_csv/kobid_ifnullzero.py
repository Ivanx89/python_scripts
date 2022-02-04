import csv
from sqlite3 import enable_shared_cache

try:

    total = 0
    string = ""
    with open("casos_VC_acum.csv", "r") as file:
        with open("casos_VC-ifzero.csv", "w") as zero:
            reader = csv.reader(file)
            for each_row in reader:
                if each_row[0] == "VC":
                    total += int(each_row[2])
                    zero.write(', '.join(each_row) + ', ' + str(total) +'\n')
                for i in range(2, 8):
                    if (len(each_row[i]) == 0) or (not each_row[i].isdecimal()):
                        each_row[i] = "0"
                        string += ',' + each_row[i]
                        zero.write(', '.join(each_row) + ', ' + str(total) +'\n')
               
                
except:
    print("ERROR")

