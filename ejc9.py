numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")