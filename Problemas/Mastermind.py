from itertools import product

def calcular_aciertos(secreto, intento):
    aciertos_directos = sum(s == i for s, i in zip(secreto, intento))
    
    from collections import Counter
    secreto_c = Counter(secreto)
    intento_c = Counter(intento)

    aciertos_indirectos = sum(min(secreto_c[n], intento_c[n]) for n in secreto_c) - aciertos_directos
    return aciertos_directos, aciertos_indirectos

def mastermind(respuesta_secreta, longitud=4, numeros=6):
    posibles = list(product(range(1, numeros+1), repeat=longitud))
    
    intentos = 0
    while posibles:
        intento = posibles[0]
        intentos += 1
        
        ad, ai = calcular_aciertos(respuesta_secreta, intento)
        
        print(f"Intento {intentos}: {intento} -> Aciertos directos: {ad}, Aciertos indirectos: {ai}")
        
        if ad == longitud:
            print(f"¡Combinación encontrada en {intentos} intentos!")
            return intento
        
        posibles = [p for p in posibles if calcular_aciertos(p, intento) == (ad, ai)]

secreto = (1, 3, 5, 5)
mastermind(secreto)

#Costo O(k^n) k= cantidad de números posibles n=longitud de la combinación