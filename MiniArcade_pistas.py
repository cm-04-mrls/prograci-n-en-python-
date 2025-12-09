# MiniArcade.py

import random
import time

def pedir_opcion():
    while True:
        op = input("Elige una opción: ").strip()
        if op in {"0", "1", "2", "3", "4"}:
            return op
        print("Tantas opciones y escoges la que no existe 🤨. Va escoge uno existente 🙄 ")



def juego_ppt():
    print("PIEDRA, PAPEL O TIJERA")
    opciones = ["piedra", "papel", "tijera"]

    while True:
        user = input("Elige piedra, papel o tijera (salir): ").lower().strip()
        if user == "salir":
            return
        
        if user not in opciones:
            print("Opción no válida")
            continue
        
        pc = random.choice(opciones)
        print(f"El ordenador eligió: {pc}")

        if user == pc:
            print("Empate")
        elif (user == "piedra" and pc == "tijera") or \
             (user == "papel" and pc == "piedra") or \
             (user == "tijera" and pc == "papel"):
            print("Waos, Ganaste! (La proxima te gano 🤫) ")
        else:
            print("JA, Perdiste! 🤣")


def juego_adivina():
    print("Adivina el número (1-20)")
    secreto = random.randint(1, 20)
    intentos_max = 5
    intentos = 0

    while intentos < intentos_max:
        try:
            n = int(input("Escribe un número: "))
        except ValueError:
            print("Enserio?, eso no es un número ")
            continue

        intentos += 1

        if n == secreto:
            print("Por fin!. Lo adivinaste!")
            return
        elif n < secreto:
            print("Prueba con un número más grande")
        else:
            print("Prueba con un número más pequeño")

    print("No lo has conseguido JA . El número era", secreto)


def juego_calculo_mental_expres(preguntas=8, tiempo_total=35):
    print("CÁLCULO MENTAL EXPRÉS")
    print(f"Te quedan {tiempo_total} segundos para {preguntas} operaciones.")

    aciertos = 0
    inicio = time.time()

    for i in range(1, preguntas + 1):
        if time.time() - inicio > tiempo_total:
            print("Tiempo agotado.")
            break

        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(["+", "-", "*"])

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        else:
            res = a * b
        
        try:
            user = int(input(f"{i}) ¿Cuánto es {a} {op} {b}? "))
        except ValueError:
            print("Respuesta inválida.")
            continue

        if user == res:
            print("Correcto.")
            aciertos += 1
        else:
            print(f"Incorrecto. Era {res}")

    print(f"Fin del test. Puntuación: {aciertos}/{preguntas}")
    return aciertos



def juego_eco_invertido():
    print("ECO INVERTIDO (pulsa ENTER vacío para salir)")
    while True:
        texto = input("Escribe algo: ")
        if texto == "":
            print("Saliendo del eco invertido...")
            return
        
        invertido = texto[::-1]
        vocales = sum(c in "aeiouAEIOU" for c in texto)

        print(f"→ Invertido: {invertido}")
        print(f"→ Caracteres: {len(texto)} | Vocales: {vocales}")


def main():
    print("Bienvenido/a al Mini Arcade 👾")
    while True:
        print("=== MINI ARCADE ===")
        print("1) Piedra, Papel o Tijera")
        print("2) Adivina el número (1-20)")
        print("3) Juego cálculo mental")
        print("4) Juego del eco invertido")
        print("0) Salir")
        
        opcion = pedir_opcion()

        if opcion == "1":
            juego_ppt()
        elif opcion == "2":
            juego_adivina()
        elif opcion == "3":
            # valores por defecto, pero puestos para que no pete
            juego_calculo_mental_expres(8, 35)
        elif opcion == "4":
            juego_eco_invertido()
        elif opcion == "0":
            print("¡Hasta luego!")
            break

        time.sleep(0.8)

if __name__ == "__main__":
    main()