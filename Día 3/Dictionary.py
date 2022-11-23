diccionario={'Key_1':'Adrian',
             'Key_2':'Vargas',
             'Key_3':'Rangel'}
print(type(diccionario))
print(diccionario)

resultado=diccionario['Key_1']
print(resultado)
diccionario_2={'c1':55,'c2':[100,20,30],'c3':{'s1':100,'s2':200}}
print(diccionario_2['c2'][1])
print(diccionario_2['c3']['s1'])
dic={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())
dic={1:'a',2:'b'}
print(dic)
dic[3]='c'#Se agrega la clave 3 con valor c al diccionario
print(dic)
dic[2]='f'
print(dic)
print(dic.keys())#imprime las claves
print(dic.values())#imprime los valores
print(dic.items())#trae todo el contenido