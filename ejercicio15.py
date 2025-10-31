numeros = []
while True:
    num = int(input("Escribe un número (0 para terminar): "))
    if num == 0:
        break
    numeros.append(num)
    
print("Lista completa:", numeros)

buscar = int(input("¿Qué número quieres buscar?: "))

posiciones = [i for i, n in enumerate(numeros) if n == buscar]

if posiciones:
    print(f"El número {buscar} aparece en las posiciones: {posiciones}")
else:
    print(f"El número {buscar} no aparece en la lista.")