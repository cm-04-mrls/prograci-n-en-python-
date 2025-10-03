print("Ingrese la primera nota:")
nota1 = float(input())
print("Ingrese la segunda nota:")
nota2 = float(input())
print("Ingrese la tercera nota:")
nota3 = float(input())

# Aplicamos las reglas del ejercicio con tu estilo de if-elif-else

if nota1 <= 4 and nota2 <= 4 and nota3 <= 4:
    print("La nota final es: 0")
elif nota1 > 4 and nota2 > 4 and nota3 > 4:
    nota_final = 0.3 * nota1 + 0.2 * nota2 + 0.5 * nota3
    print("La nota final es:", nota_final)
else:
    print("La nota final es: 2")
