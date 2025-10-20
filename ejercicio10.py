total = 0.0
while True:
    precio = float(input("Introduce un precio (0 para terminar): "))
    if precio == 0:
        break
    total += precio
print(f"Total de la factura: {total:.2f}")