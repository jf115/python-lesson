nombre = ' jose'
print(nombre)
nombre = nombre.strip() #Quita los espacios al principio o al final de la palabra
print(nombre)
nombre=nombre.capitalize()  #Pone la primer letra en mayuscula
print(nombre)
nombre=nombre.count('o')
print(nombre)
nombre='Un texto de varias palabras'
print(nombre[3])    #Me indica cuál es el valor que hay en la posición 4 de lo que esrbibí, en python se inicia a contar desde cero
print(nombre.replace('x','s'))  #replace me cambia algo que está por algo nuevo

#Slices: es rebanar el texto, sacar una parte del texto

print(nombre[0:10]) #Me da como resultado los objetos que están en esas posiciones, el resultado llega a n-1, es decir, no toma la última posición

