# Solicitar al usuario una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Inicializar contadores para vocales y consonantes
vocales = 0
consonantes = 0

# Recorrer cada caracter en la cadena
for caracter in cadena:
    # Convertir el caracter a minúscula para comparar
    caracter = caracter.lower()
    # Verificar si es una letra
    if caracter.isalpha():
        # Contar vocales y consonantes
        if caracter in "aeiou":
            vocales += 1
        else:
            consonantes += 1

# Mostrar los resultados
print(f"La cadena tiene {vocales} vocales y {consonantes} consonantes.")