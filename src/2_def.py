horas = int(input("Cuantas horas trabajas?:"))
coste = int(input("Cuanto cobras por hora?:"))

def importe_total(horas, coste):

    return coste * horas

print("Tu importe total es de ",importe_total(horas, coste))
