def Merge_Sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]


        Merge_Sort(esquerda)
        Merge_Sort(direita)
        
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k+= 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1 

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


        print(f'intercalaçao:{lista}')

dados = [8, 3, 5, 2, 9, 1]
print(f'lista original:{dados}')
Merge_Sort(dados)
print(f'lista ordenada:{dados}')        

#Pontos Positivos

#Muito eficiente (O(n log n)) Mesmo no pior caso, ele é rápido e previsível.

#Estável Mantém a ordem de elementos iguais, útil em ordenações múltiplas.

#Bom pra listas grandes ou com muitos dados aleatórios Funciona muito bem mesmo com grandes volumes.

# Pontos Negativos

#Usa memória extra Precisa criar listas auxiliares pra fazer a intercalação.

#Mais complexo de entender que os básicos (Bubble, Insertion) Usa recursão e pode ser difícil pra quem tá começando.

#Menos eficiente em listas pequenas Para poucas posições, outras técnicas simples podem ser mais rápidas.

