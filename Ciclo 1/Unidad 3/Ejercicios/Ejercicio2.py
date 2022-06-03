# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista  y los muestre por pantalla ordenados de menor a mayor.

ganadores=[]
win=[]
numero=int(input("Ingrese el numero de ganadores de la loteria: "))

print("Ingrese los numero ganadores")
for i in range(numero):
  win=int(input("Gandor:"))
  ganadores.append(win)
  ganadores.sort()
    

print("Los ganadores son:")
for i in range(len(ganadores)):
    print(ganadores[i], end=" , ")