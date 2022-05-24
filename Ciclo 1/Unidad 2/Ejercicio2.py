# Escriba un programa que simule un fondo. El programa solicitará primero una cantidad,
# que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará
# una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere
# al objetivo.

ahorro=0
dinero=float(input("Cuanto dinero desea ahorrar?: "))


while dinero>ahorro:
    deposito=float(input("Cuanto dinero desea ingresar?: "))
    if deposito < 1:
        while deposito<1:
            print("El deposito debe ser igual o mayor a 1")
            deposito=float(input("Cuanto dinero desea ingresar?: "))
    ahorro+=deposito
    print(ahorro)
print(f'¡Objetivo conseguido! Ha ahorrado usted {ahorro} Pesos.')