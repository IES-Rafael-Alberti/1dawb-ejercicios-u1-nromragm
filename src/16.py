precio_pan = 3.49

descuento = 0.60

barras_no_frescas = int(input("Ingrese el número de barras no frescas vendidas: "))

coste_total = barras_no_frescas * precio_pan * (1 - descuento)

print(f"Precio de una barra de pan: {precio_pan}€")
print(f"Descuento: {descuento * 100}%")
print(f"Coste total de las barras no frescas: {coste_total:.2f}€")