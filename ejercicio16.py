n = int(input("Introduce el tamaño N de la matriz (N x N): "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"Introduce el valor en posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

es_identidad = True
for i in range(n):
    for j in range(n):
        if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
            es_identidad = False
            break

if es_identidad:
    print("Es una matriz identidad.")
else:
    print("No es una matriz identidad.")