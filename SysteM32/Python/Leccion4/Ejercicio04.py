# Ejercicio 4: Sumar numeros pares dentro de un rango
# hacer un programa para sumar numeros pares dentro
# de un rango, por ejemplo:
#                             Suma de numeros pares del 2 al 30
#                             Suma = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0:
        suma += i
print(f"La suma de numeros pares dentro del rango es: {suma}")