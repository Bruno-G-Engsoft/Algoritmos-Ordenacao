def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def Heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    print(f'heap Maximo:{lista}')


    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
        print(f'passo {n - 1}:{lista}')
dados = [8, 0, 7, 9, 2, 4, 10, 87, 6, 20, 14]
print(f'lista original:{dados}')
Heap_sort(dados)
print(f'lista ordenada:{dados}')                        


#Pontos Positivos

#Complexidade sempre garantida: O(n log n) Mesmo no pior caso, continua eficiente.

#Não é recursivo (pode ser implementado iterativamente) Não corre o risco de stack overflow.

#Funciona bem mesmo com dados desordenados Desempenho consistente independente da entrada.

# Pontos Negativos

#Não é estável Pode mudar a ordem de elementos iguais.

#Mais difícil de implementar que os básicos Requer conhecimento de árvore binária e manipulação de índices.

#Desempenho prático menor que o Quick Sort em muitos casos Apesar da garantia teórica, pode ser mais lento em listas pequenas.