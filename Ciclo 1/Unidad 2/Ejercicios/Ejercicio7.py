# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla si es un número primo o no.

num=int(input("Ingrese un numero entero positivo: "))

for i in range(2,num):
    if i%num==0:
     break
    
if (i+1)==num:
    print("Primo")
else:
    print("No es primo")