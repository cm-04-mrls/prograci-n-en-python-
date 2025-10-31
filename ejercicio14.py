nombres = input("Introduce nombres separados por comas: ")
lista_nombres = [nombre.strip() for nombre in nombres.split(",")]
print("Lista invertida:")
print(lista_nombres[::-1])