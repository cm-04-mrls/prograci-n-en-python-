print("Pon una nota")
nota =int(input())
if nota < 0 or nota > 120 :
    print("Calificación no valida")
#else :
# if ()
elif nota < 5 :
    print("insuficiente")
elif 5 <= nota < 6:
    print("Suficiente")
elif 6 <= nota < 7:
    print("Bien")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota < 10:
     print("Sobresaliente")
else:  # Esto solo se cumple si nota == 10 (y es válida)
    print("Nota")
