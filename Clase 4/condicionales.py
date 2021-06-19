# edad = int(input('Ingrese la edad: '))

# if edad >= 18:
#     print('Es mayor de edad')
# else:
#     print('Es menor de edad')

#edad = int(input('Ingrese la edad: '))

# if edad < 10:
#     print('Muy joven')
# elif edad >=10 and edad < 14:
#     print ('Es categoria infantil')
# elif edad >=14 and edad < 17:
#     print ('Es categoria juvenil')
# elif edad >=18 and edad < 20:
#     print ('Es categoria sub 20')
# elif edad >=20:
#     print ('Es categoria profesional')

# edad1 = int(input('Ingrese edad 1: ')) Esto sobra porque ya definí la variable edades, entonces es mejor poner edades (a, b, c, d)
# edad2 = int(input('Ingrese edad 2: '))
# edad3 = int(input('Ingrese edad 3: '))
# edad4 = int(input('Ingrese edad 4: '))

def edades (edad1, edad2, edad3, edad4):
    if edad1 > edad2 > edad3 > edad4:
        print (edad1)
    elif edad2 > edad3 > edad4:
        print (edad2)
    elif edad3 > edad4:
        print (edad3)
    else:
        print (edad4)

edades(1,2,3,4)
edades(4,5,3,1)
edades(8,7,6,5)



