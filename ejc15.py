def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

try:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")