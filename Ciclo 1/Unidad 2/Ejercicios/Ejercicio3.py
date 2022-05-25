# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números
# impares desde 1 hasta ese número separados por comas.

num=int(input("Ingrese un número entero positivo: "))
if num <1:
    while num < 1:
        print("El numero debe ser positivo ")
        num=int(input("Ingrese un número entero positivo: "))
        
for i in range(num):
    if i%2!=0:
        print(i, end=",")