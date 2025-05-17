def detectar_mentirosos(opiniones):
    n = len(opiniones)
    acusaciones = [0] * n

    for i in range(n):
        for j in range(n):
            if opiniones[i][j]:
                acusaciones[j] += 1

    posibles_honestos = [i for i in range(n) if acusaciones[i] < n // 2]

    mentirosos = set()
    for honesto in posibles_honestos:
        for j in range(n):
            if opiniones[honesto][j]:
                mentirosos.add(j)

    return mentirosos

opiniones = [
    [False, True, False, True, False],  # Empleado 0 acusa a 1 y 3
    [False, False, True, False, False], # Empleado 1 acusa a 2
    [True, False, False, False, False], # Empleado 2 acusa a 0
    [False, False, False, False, True], # Empleado 3 acusa a 4
    [False, False, True, False, False]  # Empleado 4 acusa a 2
]

mentirosos = detectar_mentirosos(opiniones)

print("Empleados mentirosos detectados:", mentirosos)

#Costo O(n²)
#Como se usan matrices, en memoria estaremos usando O(n²) 