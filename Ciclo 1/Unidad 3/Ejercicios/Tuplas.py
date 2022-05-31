#Definicion tupla ->no mutable

Frutas=("Manzana","Naranja","Durazno")

#Modificar tupla -> convirtendola en lista

listaFruta=list(Frutas)

print(listaFruta)

del listaFruta[0]
print(listaFruta)

listaFruta.insert(0,"Manzana")
print(listaFruta)

#Remodificaion

Frutas=tuple(listaFruta)