palabra='python'
lista=[]
for letra in palabra:
    lista.append(letra)
print(lista)

lista_comprimida=[letra for letra in 'python']
print(lista_comprimida)

list=[n for n in range (0,10)]
print(list)

list=[n/2 for n in range (0,10)]
print(list)

list=[n for n in range (0,10) if n*2>10]
print(list)

list=[n if n*2>10 else 'no' for n in range (0,10)]
print(list)

pies =[10,20,30,40,50]
metros =[p*3.281 for p in pies]
print(metros)