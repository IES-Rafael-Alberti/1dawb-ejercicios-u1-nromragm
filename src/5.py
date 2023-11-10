importe_sin_iva = float(input("Ingresa el importe sin IVA del artículo: "))

tipo_iva = float(input("Ingresa el tipo de IVA a aplicar: "))

iva = (importe_sin_iva * tipo_iva) / 100

precio_final = importe_sin_iva + iva

print(f"El precio final del artículo es: {precio_final}€.")