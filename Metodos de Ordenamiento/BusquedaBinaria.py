def BusquedaBinaria(lista, elemento):
    inicio=0
    fin = len(lista)-1
    
    while inicio <= fin:
        medio = (inicio + fin) //2
        if lista[medio] == elemento:
           return medio
        elif lista[medio] < elemento:
             inicio = medio + 1
        else:
             fin = medio -1
        
    return -1

lista=[1,3,4,5,7,8,9]
n=8

resultado = BusquedaBinaria(lista,n)

if resultado != -1:
    print(f"elemento {n} se encuentra en la posicion {resultado}")
else:
    print(f"El elemento {n} no esta en la lista")
    
#Costo  O(log n)