def Bubble_Sort(lista):
    n = len(lista)

    for j in range(n- 1):
        for c in range(n-1):
            if lista[c] > lista[c + 1]:
                lista[c], lista[c + 1] = lista[c + 1], lista[c]

dados = [8 , 6, 3, 7, 9, 4, 5]
Bubble_Sort(dados)
print(f'dados ordenamdos:',dados)             

#Pontos Positivos

#Muito fácil de entender e implementar Ideal pra quem tá começando com algoritmos.

#Pode parar antes do final se a lista já estiver ordenada Dá pra otimizar com uma flag pra detectar se houve troca.

#Estável Mantém a ordem dos elementos iguais (importante em ordenações por múltiplos critérios).

# Pontos Negativos

#Muito lento em listas grandes Tem complexidade  O(n²) — compara e troca muito.

#Faz muitas trocas desnecessárias Troca quase toda hora, mesmo se a lista estiver quase ordenada.

#Pouco usado na prática Só é bom pra estudo; na vida real, algoritmos melhores são preferidos.