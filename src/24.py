precio = input("Escribe el precio del producto con dos decimales: ")

precio = float(precio)

euros = int(precio)
centimos = int((precio - euros) * 100)

print("Número de euros:", euros)
print("Número de céntimos:", centimos)