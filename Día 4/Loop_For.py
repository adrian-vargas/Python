lista = ['a','b','c','d']
for letra in lista:
    numero_letra=lista.index(letra)+1
    print(f"Letra {numero_letra}: {letra}")

list=['pablo','laura','fede','luis','julia']
for nombre in list:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre sin inicial l")

numeros=[1,2,3,4,5]
mi_valor=0

for numero in numeros:
    mi_valor=mi_valor+numero
    print(mi_valor)

palabra='python es genial'
for letra in palabra:
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic={'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.values():
    print(item)

for a,b in dic.items():
    print(a,b)