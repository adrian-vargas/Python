mi_tupla=(1,2,3,4,5)
print(type(mi_tupla))
print(mi_tupla)
print(mi_tupla[0])
print(mi_tupla[-1])
mi_tupla=(1,2,(3,4),5)
print(mi_tupla[2])
mi_tupla=list(mi_tupla)
print(type(mi_tupla))#casting de tupla a lista
t=(1,2,3)
x,y,z=t
print(x,y,z)
t=(1,2,3,1,1)
print(len(t))
print(t.count(1))#contar repeticiones