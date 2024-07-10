numero1 = int(input("Ingresa un numero"))
numero2 = int(input("Ingresa un numero"))
numero3 = int(input("Ingresa un numero"))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

# Mostrar el resultado
print("El número mayor es:", mayor)