palabra = 'Una palabra'
print(palabra)
lista = list(palabra)
print(lista)
diccionario = {'nombre':'Lina','Apellido':'Silva'}
lista = list(diccionario) #Asi vuelvo un diccionario en tuplas
lista = list(diccionario.keys()) #asi me salen las llvaes del diccionarioo, igual de lo que va a salir en la linea anterior
print(lista)
lista = list(diccionario.values()) #asi me salen los items del diccionario
print(lista)
lista = list(diccionario.items()) 
print(lista)
tupla = tuple(lista)
print(tupla)

#Asì convertimos una lista en un str
lista = list(palabra)
print(lista)  #aqui sale todo como una lista
palabra = ''.join(lista)  #esto me pasa de lista a str todos los elementos que contiene la lista
print(palabra)

