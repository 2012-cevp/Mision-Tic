# Escriba un programa que pregunte una y otra vez si desea continuar con el programa,
# siempre que se conteste exactamente sí (en minúsculas y con tilde)

r1="sí"
r2="no"

pregunta=input("¿Desea continuar el programa?:")

while pregunta == r1:
    pregunta=input("¿Desea continuar el programa?:")

print("¡Hasta la vista!")