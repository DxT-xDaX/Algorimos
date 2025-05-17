class Caja:
    def __init__(self, ancho, profundidad, altura):
        self.ancho = ancho
        self.profundidad = profundidad
        self.altura = altura

    def area_base(self):
        return self.ancho * self.profundidad

def rotaciones_caja(cajas):
    rotaciones = []
    for caja in cajas:
        a, b, h = caja.ancho, caja.profundidad, caja.altura
        rotaciones.append(Caja(max(a, b), min(a, b), h))
        rotaciones.append(Caja(max(a, h), min(a, h), b))
        rotaciones.append(Caja(max(b, h), min(b, h), a))
    return rotaciones

def altura_maxima(cajas):
    rot = rotaciones_caja(cajas)
    rot.sort(key=lambda c: c.area_base(), reverse=True)
    n = len(rot)
    alturas = [c.altura for c in rot]

    for i in range(1, n):
        for j in range(0, i):
            if rot[i].ancho < rot[j].ancho and rot[i].profundidad < rot[j].profundidad:
                if alturas[i] < alturas[j] + rot[i].altura:
                    alturas[i] = alturas[j] + rot[i].altura

    return max(alturas)

cajas = [
    Caja(4, 6, 7),
    Caja(1, 2, 3),
    Caja(4, 5, 6),
    Caja(10, 12, 32)
]

print("Altura máxima de la pila:", altura_maxima(cajas))
#Costo O(n²)
#Uso de memoria O(n)