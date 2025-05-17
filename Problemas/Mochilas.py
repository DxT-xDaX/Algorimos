def mochila_optimizada(pesos, valores, capacidad):
    n = len(valores)
    dp = [0] * (capacidad + 1)
    
    for i in range(n):
        for w in range(capacidad, pesos[i] - 1, -1):
            dp[w] = max(dp[w], valores[i] + dp[w - pesos[i]])

    return dp[capacidad]


pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 5

resultado = mochila_optimizada(pesos, valores, capacidad)
print("Valor máximo:", resultado)

#Costo computacional O(n * W) W=capacidad
