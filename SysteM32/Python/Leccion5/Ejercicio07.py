# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1 - 100, luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun sea mayor o menos
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos.

import random
print("\t.:Juego adivina el numero:. ")
aleatorio = random.randint(0, 100) # toma de 0 a 100 literal, generamos un num aleatorio
contador = 0
while True:
    numero = int(input("Ingrese un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, ingrese un numero menor")
    elif numero < aleatorio:
        print("\tNo es el numero, ingrese un numero mayor")
    else:
        print(f"Felicidadess, acabas de adivinar el numero {aleatorio}")
        break
print(f"\nNumero de intentos: {contador}")