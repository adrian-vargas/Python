lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for item in lista_numeros:
    if item%2==0:
        suma_pares+=item
    elif item%2==1:
        suma_impares+=item

mi_lista = list(range(1,16))
suma_cuadrados=0
cuadrado=0
for item in mi_lista:
    cuadrado=item*item
    suma_cuadrados+=cuadrado
    print(suma_cuadrados)