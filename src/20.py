numero_telefono = input("Escribe un número de teléfono en formato +34-XXXXXXXXXX-XX: ")

partes = numero_telefono.split("-")

numero_sin_prefijo = partes[1]

print(f"Número de teléfono sin prefijo: {numero_sin_prefijo}")