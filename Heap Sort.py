def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    # Construir max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrair elementos do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move maior para o final
        heapify(arr, i, 0)

    return arr


lista = [4, 10, 3, 5, 1]
heap_sort(lista)
print(lista)  # Saída: [1, 3, 4, 5, 10]

#Vantagens do Heap Sort
# Desempenho consistente
#Não usa listas auxiliares 
# (sem custo extra de memória)
#Funciona bem com dados desordenados

#Desvantagens do Heap Sort
#Não é estável
# Lento em listas pequenas
#A estrutura de heap requer mais
#  lógica do que outros métodos simples