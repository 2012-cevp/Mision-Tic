def cliente(informacion:dict)->dict:
    respuesta={}
    
    respuesta["nombre"]=informacion["nombre"]
    respuesta["edad"]=informacion["edad"]
    
    
    if respuesta["edad"]>18:
        respuesta["atraccion"]="X-Treme"  
        respuesta["apto"]=True
        respuesta["primer_ingreso"]=informacion["primer_ingreso"]
        if respuesta["primer_ingreso"]==True:
            respuesta["total_boleta"]= 20000*0.95
        else:
            respuesta["total_boleta"]= 20000
    
    if respuesta["edad"] >= 15 and respuesta["edad"]<=18:
        respuesta["atraccion"]="Carros chocones" 
        respuesta["apto"]=True
        respuesta["primer_ingreso"]=informacion["primer_ingreso"]
        if respuesta["primer_ingreso"]==True:
                respuesta["total_boleta"]= 5000*0.93
        else:
            respuesta["total_boleta"]= 5000
    
    if respuesta["edad"] >= 7 and respuesta["edad"]<15:
        respuesta["atraccion"]="Sillas voladoras" 
        respuesta["apto"]=True
        respuesta["primer_ingreso"]=informacion["primer_ingreso"]
        if respuesta["primer_ingreso"]==True:
                respuesta["total_boleta"]= 10000*0.95
        else:
            respuesta["total_boleta"]= 10000
            
    if respuesta["edad"] < 7:
        respuesta["atraccion"]="N/A" 
        respuesta["apto"]=False
        respuesta["primer_ingreso"]=informacion["primer_ingreso"]
        if respuesta["primer_ingreso"]==True:
            respuesta["total_boleta"]="N/A"
    
    return respuesta



a={"id_cliente":1,"nombre":"Johana Fernandez ","edad":20,"primer_ingreso":True}
b={"id_cliente":1,"nombre":"Johana Fernandez ","edad":20,"primer_ingreso":False}
c={"id_cliente":2,"nombre":"Gloria Suarez","edad":3,"primer_ingreso":True}
d={"id_cliente":3,"nombre":"Tatiana Suarez ","edad":17,"primer_ingreso":True}
e={"id_cliente":3,"nombre":"Tatiana Suare ","edad":20,"primer_ingreso":False}
f={"id_cliente":4,"nombre":"Tatiana Ruiz ","edad":8,"primer_ingreso":True}
g={"id_cliente":4,"nombre":"Tatiana Ruiz ","edad":8,"primer_ingreso":False}

print(cliente(a))
print(cliente(b))
print(cliente(c))
print(cliente(d))
print(cliente(e))
print(cliente(f))
print(cliente(g))