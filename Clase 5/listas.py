# numeros = [8, 5, 6]
# print(len(numeros))
# print(numeros[2])
# numeros[2]=3    #Así cambio el valor de algo sin tener que tocar toda la lista
# print(numeros)

# numeros.append(25)      #Agrego mas elementos
# print(numeros)
# print(sum(numeros))     #Suma toda la cantidad de resultados de numero que se han generado

#Cuál es el promedio mas alto
numeros1 = [59, 58+5, 45-5, 12*2]
numeros2 = [54, 58+5, 45, 12+24]
numeros3 = [54+2, 58+5, 45, 12]
numeros4 = [4, 58+5, 45*2, 12]

n1=((sum(numeros1))/len(numeros1))
n2=((sum(numeros2))/len(numeros2))
n3=((sum(numeros3))/len(numeros3))
n4=((sum(numeros4))/len(numeros4))
#print(max(n1,n2,n3,n4))        #forma corta

#Forma larga
if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print('El promedio es ', n1)
elif n2 >= n3 and n2 >= n4:
    print('El promedio es ', n2)
elif n3 >= n4:
    print('El promedio es ', n3)
else:
    print('El promedio es ', n4)