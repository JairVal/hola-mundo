# Solicitar al usuario que ingrese dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Realizar operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Manejar la división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No es posible dividir entre cero."

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)