print("Adivina el numero secreto del 1-10")
numero = int(input())
while numero < 7 or numero > 7 :
    if numero < 0 or numero > 10 :
        print("Número no valido")
        print("Escoge otro") 
        numero = int(input())
    else:
        if numero < 7 :
            print("Muy bajo")
            print("Intenta de nuevo")
            numero = int(input())
        else:
            if numero > 7 :
                print("Muy alto")
                print("Vamos hazlo otra vez")
                numero = int(input())
print("Wao por fin, adivinaste, muy bien")