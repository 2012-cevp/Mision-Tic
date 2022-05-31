#Definicion lista
lista=['Carlos','Eduardo','Villalba','Perdomo']

#Indice negativo muestra ultimo elemento de la lista
print(lista[-1])

#Imprimir un rango
print(lista[0:2]) #sin incluir el indice 2

#Imprimir todos los elementos menos el ultimo
print(lista[:-1])

# Cambiar valor
lista[0]="Hachi"
print(lista)
#Agregar un elemento a la lista de ultimas
lista.append('Carlos')
#Insertar con base a una posicion
lista.insert(1,'pedro')
#Iteracion
for i in lista:
    print(i,end=",")