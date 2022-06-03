def AutoPartes(ventas):
    dict={}
    llave=1
    
    for x in ventas:
        dict[llave]=x
        llave+=1
    return dict

def consultaRegistro(ventas,idProducto):
    respuesta=""
    en=False
    
    for i in range(1,len(ventas.keys())+1):
        if idProducto in ventas[i]:
            respuesta=respuesta+"Producto consultado : "+str(idProducto)+"  Descripción  "+ventas[i][1]+"  #Parte  "+ventas[i][2]+"  Cantidad vendida  "+str(ventas[i][3])+"  Stock  "+str(ventas[i][4])+"  Comprador "+ventas[i][5]+"  Documento  "+str(ventas[i][6])+"  Fecha Venta  "+ventas[i][7]+"\n"
            en=True 
    if en:
        print(respuesta)
    else:
        respuesta="No hay registro de venta de ese producto"
        print(respuesta)