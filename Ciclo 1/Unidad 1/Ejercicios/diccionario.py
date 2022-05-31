nombres={}
datos={"id":1,"nombre":"Carlos","edad":21,"primero":True}

# Acceder a un elemnto
print(datos["nombre"])

# Otra forma acceder a los elementos
print(datos.get("nombre"))

# Modificar elementos
datos['id']=2
print(datos)
# Llenar un diciconarios vacio
nombres["Eduardo"]=1
print(nombres)

#Recorrer elementos
for i,j in datos.items():
    print(i,j)