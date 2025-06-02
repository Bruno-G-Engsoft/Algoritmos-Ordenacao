def courting_sort(lista):
    if not lista:
        return []
    
    maior = max(lista)
    contador = [0] * (maior + 1)

    for num in lista:
        contador[num] += 1

    i = 0
    for num in range(len(contador)):
        for _ in range(contador[num]):
            lista[i] = num
            i += 1

dados = [4, 2, 2, 8, 3, 3, 1]
print(f'original:{dados}')
courting_sort(dados)
print(f'ordenado:{dados}')        


#Pontos Positivos

#Muito rápido (O(n + k)) Quando k (o maior número) é pequeno, é super eficiente.

#Estável Mantém a ordem dos elementos iguais.

#Simples e direto Fácil de implementar para números inteiros.

#Pontos Negativos

#Só funciona com inteiros não-negativos

#Consome muita memória se o maior número for muito grande

#Não funciona bem com números decimais ou negativos

