def mcd(a,b):
    if a < b:
        menor = a
    else:
        menor = b
    
    for divisor in range(menor, 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        
def esPrimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print("El MDC de 20 y 12 es:", mcd (20,12))

print("Número primos del 1 al 50:")

for numero in range(1,51):
    if esPrimo(numero):
        print(numero, end=" ")
print()