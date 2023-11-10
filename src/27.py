nombre_producto = input("Introduce el nombre del producto: ")

precio_unitario = float(input("Introduce el precio unitario del producto: "))

num_unidades = int(input("Introduce el número de unidades: "))

coste_total = precio_unitario * num_unidades

cadena_formateada = "{} - Precio Unitario: {:>9.2f} - Unidades: {:>3} - Coste Total: {:>11.2f}".format(
    nombre_producto, precio_unitario, num_unidades, coste_total
)

print(cadena_formateada)