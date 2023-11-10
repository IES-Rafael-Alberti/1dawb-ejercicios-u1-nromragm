fecha = input("Escribe tu fecha de nacimiento (dd/mm/aaaa): ")

partes_fecha = fecha.split("/")

dia = partes_fecha[0]
mes = partes_fecha[1]
año = partes_fecha[2]

print("Día:", dia)
print("Mes:", mes)
print("Año:", año)