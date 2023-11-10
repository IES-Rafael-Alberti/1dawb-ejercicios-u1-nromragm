
"""
Inicio
Escribe "Ingresa el primer número entero: "
Lee numero1
Escribe "Ingresa el segundo número entero: "
Lee numero2

Si numero1 == numero2 hacer
    Escribe "Error: Los números no pueden ser iguales"
Sino
    Si numero1 < numero2
        menor = numero1
    Sino
        menor = numero2
Fin        
"""

num1 = int(input("Ingresa un  numero entero: "))
num2 = int(input("Ingresa un  numero entero: "))

if num1  == num2:
    print("Los números no pueden ser iguales.")
else:
    menor = min(num1, num2)
    mayor = max(num1, num2)
    diferencia = (mayor - menor)

print(f"el numero menor es {menor} y entre ellos existen {diferencia} numeros enteros")