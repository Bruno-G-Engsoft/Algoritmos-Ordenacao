def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

#Vantagens do Insertion Sort

#simplicidade de implementação
#eficiência em listas que já estão parcialmente ordenadas

#Desvantagens do Insertion Sort
#mais lento do que outros algoritmos de ordenação 
#em listas grandes e desordenadas.

#necessidade de espaço adicional para realizar
#  as operações de deslocamento dos elementos.