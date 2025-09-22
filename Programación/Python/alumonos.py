print("Dame el número de los chicos de la clase")
chicos=int(input())
print("Dame el número de las chicas de la clase")
chicas=int(input())

total = chicos+chicas
pchicas=(chicas/total)+100
pchicos=(chicos/total)+100

print("RESUMEN")
print(f"Él número total de alumnos es{total}")

print("EL porcentaje de las chicas es de %.2f %%"%{pchicas})

print(f"EL porcentaje de las chicas es de {pchicos:.2f}%")

