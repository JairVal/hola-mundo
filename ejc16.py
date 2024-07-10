def generar_numeros_aleatorios():
    numeros_aleatorios = []
    # Elegir un valor arbitrario como semilla
    semilla = 987654321
    a = 1664525
    c = 1013904223
    m = 2**32

    for _ in range(5):
        # Generar el siguiente número pseudoaleatorio
        semilla = (a * semilla + c) % m
        numero_aleatorio = semilla % 100 + 1  # Ajustar el rango a [1, 100]
        numeros_aleatorios.append(numero_aleatorio)

    return numeros_aleatorios

numeros_aleatorios = generar_numeros_aleatorios()
print("5 números aleatorios entre 1 y 100:")
print(numeros_aleatorios)