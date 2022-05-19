
def CDT(nombre:str,capital:int,tiempo:int):
    if tiempo >=3:
        valorIntereses=(capital*0.03*tiempo)/12
        valorTotal=valorIntereses + capital
        return f'Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}'
         
    else:
        valorPerder=capital*0.02
        valorTotal= capital - valorPerder
        return f'Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}'
        
nombre=input("usuario: ")
capital=int(input("monto a ingresar: "))
tiempo=int(input("tiempo del CDT: "))

print(CDT(nombre,capital,tiempo))


