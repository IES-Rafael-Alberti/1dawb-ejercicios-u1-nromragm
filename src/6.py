importe_final =  float(input("Ingresa el importe final del artículo: "))

iva = importe_final * 0.10

importe_sin_iva = importe_final - iva

print(f"El importe sin IVA es: {importe_sin_iva}€")
print(f"El IVA pagado es: {iva}€")