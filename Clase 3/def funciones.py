# def calcular_doble(numero):
#     print(numero*2)

# calcular_doble(10) 
# calcular_doble('hi ') #Sirve también para multiplicar str, los repite

# def calculo(dato:int):
#     print(dato*3) #la funcion de esto es utilizar el parametro dat, dato no va a servir mas fuera de este espacio

# calculo(int(input('Ingresa un dato: ')))    #Memultiplica un numero
# calculo(input('Ingresa un dato: '))         #Me multiplica un str

# def total(n1, n2, n3):
#     return n1+n2+n3

# total(5,4,4)

def tiempo(entraron, salieron):
    tiempo_in = entraron*2
    tiempo_out = salieron*1
    tiempo_viaje = (90/30)*60
    return tiempo_in+tiempo_out+tiempo_viaje

print('El bus se demora en llegar', round((tiempo(int(input('Ingrese el numero de pasajeros que ingresaron: ')), (int(input('Ingrese el numero de pasajeros que se bajaron: '))))/60),2), 'horas')