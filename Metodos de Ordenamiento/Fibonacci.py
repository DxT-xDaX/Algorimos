def FibonacciR(x):
    if x==1:
     return 1

    if x==2:
        return 1
    return FibonacciR(x-2)+FibonacciR(x-1)

def Fibonacci(x):
    lista=[1,1]
    for i in range (0,x-2):
        res=lista[i]+lista[i+1]
        lista.append(res)
        print(lista[-1])

print(FibonacciR(10)) #Funcion con recursividad         Costo Computacional (2^n)
Fibonacci(10) #Funcion con listas
