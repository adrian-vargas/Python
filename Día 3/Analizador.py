word=input("Ingresa un texto\n")
letters=input("Ingresa 3 letras\n")
print("La letra " + str(letters[0]) + " aparece " + str(word.lower().count(letters[0])) + " veces")
print("La letra " + str(letters[1]) + " aparece " + str(word.lower().count(letters[1])) + " veces")
print("La letra " + str(letters[2]) + " aparece " + str(word.lower().count(letters[2])) + " veces")

lista=list(word.split())
print("Hay "+str(len(lista)) + " palabras")
start=word[0]
end=word[-1]
print(start)
print(end)
print("La primera letra es:" +str(start)+"\nLa última letra es: "+str(end))
reverso=list(word)
reverso.reverse()
reverso="".join(reverso)
print(reverso)
minus=word.lower()

diccionario={True:"Existe Python",False:"No se encuentra Python"}
python=diccionario["python" in minus]
print(python)
if "python" in minus:
    print("Existe Python")
else:
    print("No se encuentra Python")
