# Solicitar una cadena de texto al usuario
cadena = input("Ingresa una cadena de texto: ")

# Eliminar espacios y convertir a minúsculas
cadena = cadena.replace(" ", "").lower()

# Verificar si la cadena es un palíndromo
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")