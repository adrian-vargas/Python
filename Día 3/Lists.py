mi_lista=['a','b','c']
otra_lista=['hola',2,-5,'a']
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[0:2])
print(mi_lista[1:])
mi_lista_2=['d','e','f']
mi_lista_3=mi_lista+mi_lista_2
print(mi_lista_3)
mi_lista_3[0]='alfa'
print(mi_lista_3)
mi_lista_3.append('g')
print(mi_lista_3)
mi_lista_3.pop()#remueve elementos de la lista (el último por defecto)
print(mi_lista_3)
mi_lista_3.pop(0)
print(mi_lista_3)
eliminado=mi_lista_3.pop(1)#Aquí estoy conservando el elemneto eliminado en una variable
print(mi_lista_3)
print("Elemento eliminado: "+eliminado)
lista=['u','e','a','i','o']
lista.sort()
print(lista)
lista.reverse()
print(lista)
