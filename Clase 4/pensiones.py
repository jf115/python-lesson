#Anidacion
#Ejercicio para pension de una persona

edad = int(input('Ingrese la edad: '))
genero = input('Ingrese el genero: ')
semanas = int(input('Ingrese las semanas: '))

if genero == 'M':
    if edad >= 62:
        if semanas >= 250:
            print ('Se puede pensionar')
        else:
            print('Le faltan '+str(250-semanas)+ ' semanas') 
    else:
        print ('Le faltan '+str(62-edad)+ ' años')
elif genero == 'F':
    if edad >= 58:
        if semanas >= 250:
            print ('Se puede pensionar')
        else:
            print('Le faltan '+str(250-semanas)+ ' semanas') 
    else:
        print ('Le faltan '+str(62-edad)+ ' años')
else:
    print('Genero no valido')