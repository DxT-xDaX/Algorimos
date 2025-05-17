def bucketSort(Lista):
    bucket = []
    for i in range(len(Lista)):
        bucket.append([])
    for j in Lista:
        index_b = int(j/10)
        bucket[index_b].append(j)
    for i in range(len(Lista)):
        bucket[i] = sorted(bucket[i])
    k=0
    for i in range(len(Lista)):
        for j in range(len(bucket[i])):
            Lista[k] = bucket[i][j]
            k+=1
    return Lista

Lista=[1,3,5,7,78,4,13,5,76,5]
print("Lista ordenada:")
print(bucketSort(Lista))

#Costo computacional O(n log n)