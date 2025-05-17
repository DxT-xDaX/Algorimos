def es_seguro(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or \
           abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def resolver_reinas(tablero, fila):
    n = len(tablero)
    if fila == n:
        return True 

    for col in range(n):
        if es_seguro(tablero, fila, col):
            tablero[fila] = col
            if resolver_reinas(tablero, fila + 1):
                return True
            tablero[fila] = -1  

    return False

def mostrar_tablero(tablero):
    n = len(tablero)
    for i in range(n):
        fila = ['.'] * n
        fila[tablero[i]] = 'Q'
        print(' '.join(fila))
    print()

n = 8
tablero = [-1] * n
if resolver_reinas(tablero, 0):
    mostrar_tablero(tablero)
else:
    print("No se encontró solución.")
    
#Costo en el peor caso O(n!)