def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivô = lista[-1]  
    menores = [x for x in lista[:-1] if x <= pivô]
    maiores = [x for x in lista[:-1] if x > pivô]

    return quick_sort(menores) + [pivô] + quick_sort(maiores)

# Vantagens do Quick Sort
#Melhor opção para ordenar vetores grandes
#Muito rápido por que o laço interno é simples
#Memória auxiliar para a pilha de recursão é pequena

# Desvantagens do Quick Sort

#Instável
#Depende do pivô
#Pior caso é quadrático