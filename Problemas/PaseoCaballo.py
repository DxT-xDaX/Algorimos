def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

def resolver_caballo(x, y, mov_num, tablero):
    if mov_num == N * N:
        return True

    for i in range(8):
        sig_x = x + mov_x[i]
        sig_y = y + mov_y[i]

        if es_valido(sig_x, sig_y, tablero):
            tablero[sig_x][sig_y] = mov_num
            if resolver_caballo(sig_x, sig_y, mov_num + 1, tablero):
                return True
            tablero[sig_x][sig_y] = -1 

    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(f"{cel:2}" for cel in fila))
    print()
    
N = 8
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

tablero = [[-1 for _ in range(N)] for _ in range(N)]

inicio_x, inicio_y = 0, 0
tablero[inicio_x][inicio_y] = 0


if resolver_caballo(inicio_x, inicio_y, 1, tablero):
    imprimir_tablero(tablero)
else:
    print("No se encontró solución.")
    
#Costo O(k^n) k=dimension del tablero, en este caso 8x8