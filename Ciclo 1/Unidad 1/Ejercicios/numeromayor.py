#. Escribir un algoritmo que lea cuatro números e indique cual es el mayor

a=int(input("Ingrese numero 1: "))
b=int(input("Ingrese numero 2: "))
c=int(input("Ingrese numero 3: "))
d=int(input("Ingrese numero 4: "))

if a > b and a > c and a > d:
    print("El muero mayor es: ",a)

elif b>a and b > c and b > d:
     print("El muero mayor es: ",b)

elif c > a and c > b and c > d:
    print("El muero mayor es: ",c)

elif d > a and d > b and d > c:
    print("El muero mayor es: ",d)