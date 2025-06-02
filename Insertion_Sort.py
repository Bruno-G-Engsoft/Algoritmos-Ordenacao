def insertion_sort(lista):
    for c in range(1, len(lista)):
        chave = lista[c]
        j = c - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave
        print(f'passos {c}: {lista}')

dados = [5, 8, 10, 7, 6, 0, 27, 36, 97, 100]
print(f'lista original: {dados}')
insertion_sort(dados)
print(f'lista ordenada:{dados}')

# Pontos Positivos

#Muito eficiente para listas pequenas ou quase ordenadas Se a lista já está quase certa, ele vai rapidinho.

#Simples de implementar e entender Ideal pra aprender lógica de ordenação.

#Estável Mantém a ordem de elementos iguais, útil em ordenações múltiplas (ex: nome + idade).

#Pontos Negativos

#Ineficiente em listas grandes desordenadas Tem complexidade O(n²) no pior caso

#Muitas comparações e movimentações Se os elementos estiverem longe da posição correta, ele trabalha muito.

#Não ideal pra dados aleatórios em larga escala Existem algoritmos mais rápidos como Merge, Quick e Heap Sort.

