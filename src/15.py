capital_inicial = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))

tasa = 0.04

primer_año = round(capital_inicial * (1 + tasa), 2)
segundo_año = round(primer_año * (1 + tasa), 2)
tercer_año = round(segundo_año * (1 + tasa), 2)

print(f"Ahorros después del primer año: ${primer_año}")
print(f"Ahorros después del segundo año: ${segundo_año}")
print(f"Ahorros después del tercer año: ${tercer_año}")