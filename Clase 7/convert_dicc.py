#Pasar de lista a diccionario - 

# A partir de comprehension
from typing import TextIO


tripulantes = ['Jose', ' Manuel', 'Cami', 'Fer']
tripulantes_dict = {tripulante : '5' for tripulante in tripulantes}
print(tripulantes_dict)

#Por medio de la funcion fromkeys
tripulantes_dict = dict.fromkeys(tripulantes, 5)
print(tripulantes_dict)

#Por medio de la funcion zip
tripulantes_dict = dict(zip(tripulantes, range(0,len(tripulantes))))
print(tripulantes_dict)
