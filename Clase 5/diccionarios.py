# diccionario = {'clave':'valor'}
# print (diccionario['clave'])

# diccionario = {'nombre1':'Jose','edad2':25, 'lenguajes':{1:'Python',2:'PHP',3:'Java',4:'Java'}}
# print (diccionario['lenguajes'][2])
# print (len(diccionario))
# print (len(diccionario['lenguajes']))
# print (len(diccionario['lenguajes'][1]))

autos = {'autos':{'marca1':'Chevrolet','modelos':{1:'Onix',2:'Clio',3:'Tropper'},
                  'marca2':'Toyota','modelos':{1:'Prado',2:'TXL',3:'Corola',4:'4runner'},
                  'marca3':'Mazda','modelos':{1:'Mazda 2',2:'CX5'}}}

#Cuál marca tiene mas modelos

#if len(autos[marca1]) >= len(autos[marca2]) and len(autos[marca3])
print(autos['autos']['marca1'])