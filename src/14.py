num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_payasos = num_payasos * 112
peso_muñecas = num_muñecas * 75
peso_total = peso_payasos + peso_muñecas


print(f"El peso total del paquete será de {peso_total} gramos.")