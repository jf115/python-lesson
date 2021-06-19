#estatura = input('Digite su estatura: ')
#print('Su estatura es '+estatura)

#sueldo = int(input('Digite su sueldo: '))
#print('Su sueldo es '+str(sueldo+200000)) #Asi se hace porque se debe concatenar variables del mismo tipo, por eso se conectan con el +

# precio = int(input('Ingrese el valor del producto: '))
# iva = float(0.19)
# valor_iva = iva*precio
# print('El valor del iva es '+str(valor_iva))
# #total = float(precio + valor_iva)
# #print('El precio total del producto es',total)

nota_1 = float(input('Ingrese la nota 1: ')); nota_2 = float(input('Ingrese la nota 2: ')); nota_3 = float(input('Ingrese la nota 3: '))
promedio = float((nota_1+nota_2+nota_3)/3)
print('El promedio de la materia es: ', round(promedio,1))