nombre=input("Ingresa tu nombre: ")
ventas=input("Ingresa el monto de tus ventas: ")
comision=float(ventas)*0.13
print(f"Ok {nombre}.\nEste mes ganaste ${round(comision,2)}")