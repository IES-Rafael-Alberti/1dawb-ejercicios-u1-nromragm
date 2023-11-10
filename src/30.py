inicio = int(input("Ingrese un número de inicio: "))

incremento = int(input("Ingrese un incremento: "))

if incremento <= 0:
    print("Error: El incremento debe ser mayor que cero")

total = int(input("Ingrese el total de la serie: "))

if total <= 0:
    print("Error: El total debe ser mayor que cero")

serie = str(inicio) + "-"

for i in range(1, total):
    inicio += incremento
    serie += ".." + str(inicio)


print(f"Serie =>{serie}-{inicio}")