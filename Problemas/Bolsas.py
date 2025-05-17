def empaquetado_minimo(pesos, capacidad_bolsa):
    pesos_ordenados = sorted(pesos, reverse=True)

    bolsas = [] 

    for peso in pesos_ordenados:
        colocado = False
        for i in range(len(bolsas)):
            if bolsas[i] + peso <= capacidad_bolsa:
                bolsas[i] += peso
                colocado = True
                break
        if not colocado:
            bolsas.append(peso)

    return len(bolsas), bolsas

pesos = [4, 8, 1, 4, 2, 1, 3, 7]
capacidad = 10

bolsas_usadas, contenido = empaquetado_minimo(pesos, capacidad)

print("Número mínimo de bolsas usadas:", bolsas_usadas)
print("Contenido de cada bolsa:", contenido)
#Costo O(n²) peor caso, 