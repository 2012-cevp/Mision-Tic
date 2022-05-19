"""Solicitar al usuario por teclado el Alto y Ancho del Rectángulo para 
calcular el Area y Perimetro"""

alto=int(input("Ingrese el Alto del rectangulo: "))
ancho=int(input("Ingrese el Ancho del rectangulo: "))

area= alto*ancho
perimetro=(alto+ancho)*2

print(f'El area del rectangulo es: {area} \ny el perimetro es: {perimetro}')