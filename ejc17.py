def calcular_imc(peso, altura):
    return peso / (altura ** 2)

try:
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))

    if peso <= 0 or altura <= 0:
        print("El peso y la altura deben ser valores positivos.")
    else:
        imc = calcular_imc(peso, altura)
        print("Tu Índice de Masa Corporal (IMC) es: {:.2f}".format(imc))
        if imc < 18.5:
            print("Tienes un peso bajo.")
        elif imc < 25:
            print("Tienes un peso normal.")
        elif imc < 30:
            print("Tienes sobrepeso.")
        else:
            print("Tienes obesidad.")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos para el peso y la altura.")