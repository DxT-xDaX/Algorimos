def factorial(x):
    num = x
    res = 1

    for i in range(1, num + 1):
        res = res * i
    print(res)

def factorialR(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x * factorialR(x - 1)


# Pruebas
factorial(4)     # Funcion sin recursividad salida: 24
print(factorialR(5))    # Funcion con recursividad salida: 120
#Costo computacional n!