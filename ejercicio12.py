numeros = input("Escribe varios números separados por espacios: ")

lista = numeros.split()
suma = 0

for n in lista:
    suma += int(n)

print("La suma total es:", suma)