def emparejamiento_estable(entrenadores, pokemones, preferencias_entrenadores, preferencias_pokemones):
    n = len(entrenadores)
    libre_entrenadores = list(entrenadores)  
    parejas = {}  
    propuestas = {e: [] for e in entrenadores}  

    while libre_entrenadores:
        e = libre_entrenadores[0]  

        for p in preferencias_entrenadores[e]:
            if p not in propuestas[e]:
                propuestas[e].append(p)

                if p not in parejas:
                    parejas[p] = e
                    libre_entrenadores.pop(0)
                else:
                    e_actual = parejas[p]
                    if preferencias_pokemones[p].index(e) < preferencias_pokemones[p].index(e_actual):
                        parejas[p] = e
                        libre_entrenadores.pop(0)
                        libre_entrenadores.append(e_actual)  
                break

    return parejas

entrenadores = ["Ash", "Misty", "Brock"]
pokemones = ["Pikachu", "Staryu", "Onix"]

preferencias_entrenadores = {
    "Ash": ["Pikachu", "Staryu", "Onix"],
    "Misty": ["Staryu", "Pikachu", "Onix"],
    "Brock": ["Onix", "Pikachu", "Staryu"]
}

preferencias_pokemones = {
    "Pikachu": ["Ash", "Misty", "Brock"],
    "Staryu": ["Misty", "Ash", "Brock"],
    "Onix": ["Brock", "Ash", "Misty"]
}

parejas = emparejamiento_estable(entrenadores, pokemones, preferencias_entrenadores, preferencias_pokemones)

for p, e in parejas.items():
    print(f"{e} queda emparejado con {p}")

#Costo O(n²)
#Memoria O(n) para almacenar listas