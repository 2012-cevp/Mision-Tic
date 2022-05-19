# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

nHorasTrabajadas=int(input("Ingrese el numero de horas trabajadas: "))
valorHora=float(input("Ingrese el valor por hora: "))

print("Su sueldo es: ",nHorasTrabajadas*valorHora)