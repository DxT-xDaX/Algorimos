def QuickSort(Lista):
    if(len(Lista)>1):
        pivote=EncontrarPivote(Lista)
        men,may=Divide(Lista,pivote)
        men=QuickSort(men)
        may=QuickSort(may)
        return men+may
    return Lista

def EncontrarPivote(Lista):
    return sum(Lista)/len(Lista)

def Divide(Lista,pivote):
    men=[]
    may=[]
    for e in Lista:
        if(e>pivote):
            may.append(e)
        else:
            men.append(e)
    return men,may

Lista = [100, 24, 567, 2, 3, 80, 53, 798, 235, 97]
resultado = QuickSort(Lista)
print("Lista ordenada:", resultado)
#Costo computacional = O(n log n) en el peor de los casos si la lista queda desequilibrada seria de O(n²)