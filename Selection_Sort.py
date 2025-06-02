def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Assume que o menor valor está na posição atual
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        # Troca os elementos
        lista[i], lista[menor] = lista[menor], lista[i]

# Exemplo de uso
dados = [28, 65, 20, 34, 57]
selection_sort(dados)
print("Lista ordenada:", dados)

#Pontos Positivos

#Simples de entender e implementar O algoritmo é direto: procura o menor valor e coloca no lugar certo.

#Poucas trocas (swaps) Mesmo que compare bastante, ele só troca quando necessário (no máximo uma vez por posição).

#Não precisa de memória extra (in-place) Ele organiza a lista sem precisar criar outra lista, economizando memória.

#Pontos Negativos

#Lento para listas grandes Complexidade é O(n²), ou seja, fica bem devagar com muitos elementos.

#Ignora se a lista já está quase ordenada Mesmo se a lista estiver quase no jeito, ele ainda faz todas as comparações.

#Não é estável (por padrão) Se dois valores forem iguais, ele pode trocar a ordem deles na lista final — isso pode ser ruim em alguns contextos (tipo ordenação por nome e idade).