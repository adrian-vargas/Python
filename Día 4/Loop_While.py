monedas = 5
while monedas>0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else: print("No tengo más dinero")

respuesta ="s"
while respuesta=="s":
    respuesta=input("Quieres seguir? (s/n)")
else: print("Gracias")

nombre=input("Tu nombre: ")
for letra in nombre:
    if letra=="r":
        break
    print(letra)
for letra in nombre:
    if letra=="r":
        continue
    print(letra)

answer="s"
while answer=="s":
    pass
print("Hola")