
import os


lineas = os.popen("dir").readlines()

print(lineas)

for l in lineas:
    l = l.strip()
    print(lineas)