def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    if not arr:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    
    for num in arr:
        index = int(num * n) 
        buckets[index].append(num)

    
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(arr))
#Vantagens:
#Muito eficiente com entradas distribuídas uniformemente

#Pode alcançar tempo linear em condições ideais

#Simples de entender e implementar para casos específicos
#Desvantagens:
#Depende da distribuição dos dados

#Requer função de hash ou mapeamento eficaz para distribuir bem os valores

#Não é bom para valores com distribuição concentrada ou dispersa de forma desigual

#Precisa de espaço extra para os baldes