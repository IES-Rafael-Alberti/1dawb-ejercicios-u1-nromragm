frase = input("Escribe frase: ")

vocal = input("Escribe una vocal: ")

vocal_mayuscula = vocal.upper()

frase_vocal_mayuscula = frase.replace(vocal, vocal_mayuscula)

print("Frase con la vocal en mayúscula:", frase_vocal_mayuscula)