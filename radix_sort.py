def counting_sort_digito(lista, digito):
    n = len(lista)
    output = [0] * n
    contador = [0] * 10

    
    for i in range(n):
        indice = (lista[i] // digito) % 10
        contador[indice] += 1

   
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    
    i = n - 1
    while i >= 0:
        indice = (lista[i] // digito) % 10
        output[contador[indice] - 1] = lista[i]
        contador[indice] -= 1
        i -= 1

    
    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista):
    if not lista:
        return

    maior = max(lista)
    digito = 1

    while maior // digito > 0:
        counting_sort_digito(lista, digito)
        print(f"Depois de ordenar pelo dígito {digito}: {lista}")
        digito *= 10


dados = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original:", dados)
radix_sort(dados)
print("Ordenada:", dados)


#Pontos Positivos

#Muito eficiente com números inteiros grandes Especialmente quando os números têm muitos dígitos, mas o número total de elementos não é gigantesco.

#Não usa comparação direta entre os números Isso pode ser uma vantagem dependendo do contexto.

#Estável Mantém a ordem de elementos iguais, desde que o algoritmo auxiliar (como Counting Sort) também seja estável.

# Pontos Negativos

#Só funciona com inteiros (ou precisa adaptar muito pra strings e decimais).

#Consome memória extra Por usar Counting Sort várias vezes.

#Pode ser lento se os números tiverem muitos dígitos e a lista for pequena Às vezes outros algoritmos são mais simples e mais rápidos em listas menores.

