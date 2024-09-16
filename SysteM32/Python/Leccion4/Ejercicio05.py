# Ejercicio 5: factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero positivo

num = int(input("Ingrese un num: "))
while num < 0:
    print("Ingrese un num positivo!")
    num = int(input("Ingrese un num: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"El factorial del num {num} ingresado es: {factorial}")