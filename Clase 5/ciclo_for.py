numeros = [54, 63, 45, 12, 57, 84, 64, 25]

# for numero in numeros:   #Esto sirve para ir a CADA ELEMENTO
#     if numero % 2 ==0:   #Acá solo me va a mostrar los número pares
#         print(numero)
#     if numero >50:       #Muestra solo numeros mayores a 50
#         print(numero)

#Voy a scar la cedula de cada persona
devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}]

# for bd in devs:
#     print(bd['cc'])

# #Voy a sacar el mayor salario
# salario=0
# for bd in devs:
#     if bd['salario']>salario:
#         salario=bd['salario']
# print(salario)

# # sacar el nombre y cedula el mejor pago - no lo entendí
# salario=0
# dev={}
# for bd in devs:
#     if bd['salario']>salario:
#         salario=bd['salario']
#     dev=bd
# print(dev['cc'],dev['nombre'])

i=0
exp = {}
while i < len(devs):
    if i == 0:
        exp = devs[0]
    if exp ['years'] < devs [i]['years']:
        exp = devs[i]
    i+=1

#i=0 menor_exp = 10 while i< len(devs): if devs[i]["years"] < menor_exp: menor_exp = devs[i]["years"] i += 1 print ("El desarrollador con menor experiencia tiene: " + str(menor_exp) + " año(s) de experiencia")

