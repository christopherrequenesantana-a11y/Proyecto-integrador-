# Juego: Adivina el Número

print("Piensa un número del 1 al 100")
input("Presiona Enter para continuar")

minimo = 1
maximo = 100
intentos = 0

while True:

    numero = (minimo + maximo) // 2
    intentos += 1

    print("¿Tu número es", numero, "?")

    respuesta = input(
        "Escribe mayor, menor o correcto: "
    )

    if respuesta == "correcto":
        print(
            "Adiviné tu número en",
            intentos,
            "intentos"
        )
        break

    elif respuesta == "mayor":
        minimo = numero + 1

    elif respuesta == "menor":
        maximo = numero - 1
