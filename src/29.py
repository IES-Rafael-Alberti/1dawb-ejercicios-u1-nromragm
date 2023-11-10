"""
Inicio

Escribe "Ingresa tu nombre: "

Si nombre = "" hacer
nombre = Desconocido
Escribe "Ingresa tu edad: "
Lee edad

Mientras sea verdadero

Si edad >= 0 y edad <= 125 hacer
    Terminar
Sino
    Escribe "La edad debe estar entre 0 y 125 años. Intentalo de nuevo."

años = 125 - (edad)

Escribe "Te llamas (nombre) y tienes (edad) años, te quedan aún (años) años por cumplir."

Fin        
"""
nombre = input("Ingresa tu nombre: ")

if nombre == "":
    nombre = "Desconocido"
    
while True:
    edad = int(input("Ingresa tu edad (entre 0 y 125 años): "))
    if 0 <= edad <= 125:
        break
    else:
        print("La edad debe estar entre 0 y 125 años. Intentalo de nuevo.")

años = 125 - edad

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años} años por cumplir.")