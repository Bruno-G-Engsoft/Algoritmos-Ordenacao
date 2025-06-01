def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        
        merge_sort(esquerda)
        merge_sort(direita)

        
        i = j = k = 0

        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

    
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista


 #Vantagens do Merge Sort
#Muito eficiente: sempre O(n log n).

#Estável: mantém a ordem relativa dos elementos iguais.

#Funciona muito bem com listas grandes.

#Ideal para dados armazenados em arquivos (onde se lê em blocos).

#Desvantagens
#Requer memória extra proporcional ao tamanho da lista.

#Pode ser mais lento que algoritmos in-place para listas pequenas.

