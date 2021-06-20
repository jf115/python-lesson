# lista = [5, 4, 6, 8]
# matriz = [lista, lista, lista]
#print(matriz)
#for fila in matriz:
    #print(fila)
    # print(max(fila))
    # print(min(fila))
    # print(sum(fila)/len(fila))
    # print(matriz[2])

# matriz = [[5, 4, 6, 8],[7, 4, 6, 2],[5, 3, 1, 9]]

# print(matriz[0])
# print(matriz[0][2])
# print(matriz[-1][-1])
# matriz[-1][-1] = 5
# print(matriz[-1])

matriz = [[5, 7, 6, 9], [3, 4, 2, 8], [7, 9, 6, 1]]

i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        print(matriz[i][j]) #Asi me salen todos los valores de la matriz 1 a 1
        if matriz[i][j] > 4: #Asi me saldrían los valores mayores a 4
            print(matriz[i][j])
        if matriz[i][j] < 4:
            print(matriz[i][j]**matriz[i][j])
        j+=1    
    i+=1

    