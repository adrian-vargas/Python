nombres = ['Ana','Hugo','Luis']
edades = [65,29,42,55]
ciudades = ['Lima','Mexico','Madrid']
asignacion = list(zip(nombres,edades,ciudades))
print(asignacion)

for nombre,edad,ciudad in asignacion:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")

spanish=['uno','dos','tres','cuatro','cinco']
portuguese=['um','dois','três','quatro','cinco']
english=['one','two','three','four','five']

list=list(zip(spanish,portuguese,english))

print(list)

