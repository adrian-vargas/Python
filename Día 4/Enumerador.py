lista = ['a','b','c']
indice=0

for item in lista:
    print(indice,item)
    indice+=1

for indice,item in enumerate(lista):
    print(indice,item)

for indice,item in enumerate(range(50,55)):
    print(indice,item)

mis_tuples=list(enumerate(lista))
print(mis_tuples[2][0])

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for item in lista_nombres:
    if item[0]=="M":
        print(item)