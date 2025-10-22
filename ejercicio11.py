n = int(input("¿Cuántos números vas a escribir? "))

mayor = 0
menor = 9999999  

for i in range(n):
    num = int(input("Escribe un número: "))
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print("El mayor es", mayor)
print("El menor es", menor)
