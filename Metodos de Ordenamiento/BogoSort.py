import numpy as np

def ordenado(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True  

def ordena(L):
    intentos = 0
    while not ordenado(L):
        np.random.shuffle(L)
        intentos += 1
    print(f"Lista ordenada después de {intentos} intentos.")
    return L

L = [1, 23, 345, 78, 345, 78, 8, 53, 123, 567, 78, 4, 26, 7]
res = ordena(L)
print("Lista ordenada:", res)
#Costo computacional O(n*n!)