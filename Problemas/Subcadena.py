def subcadena_comun_mas_larga(cadenas):
    if not cadenas:
        return ""

    base = min(cadenas, key=len)
    longitud = len(base)

    for l in range(longitud, 0, -1): 
        for i in range(longitud - l + 1): 
            subcadena = base[i:i+l]
            if all(subcadena in s for s in cadenas):
                return subcadena

    return ""

cadenas = ["computacion", "automatica", "comunicacion"]
resultado = subcadena_comun_mas_larga(cadenas)
print("Subcadena común más larga:", resultado)
#Costo O(k × l³) k=numero de cadenas l=longitud de la cadena mas corta
#En memoria solo se usa una cadena a la vez O(1)