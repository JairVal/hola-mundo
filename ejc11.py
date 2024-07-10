def suma_naturales(limite):
    suma = 0
    for i in range(1, limite + 1):
        suma += i
    return suma

limite = int(input("Introduce un número límite: "))

resultado = suma_naturales(limite)
print("La suma de todos los números naturales hasta", limite, "es:", resultado)