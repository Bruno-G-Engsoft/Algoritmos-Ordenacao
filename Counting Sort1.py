def counting_sort(arr):
    if not arr:
        return arr

    
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    
    count = [0] * range_val

    
    for num in arr:
        count[num - min_val] += 1

    
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    
    output = [0] * len(arr)
    for num in reversed(arr):  
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


vetor = [4, 2, 2, 8, 3, 3, 1]
ordenado = counting_sort(vetor)
print(ordenado)

#Vantagem

#rapido faixa de dados pequena
#estavel
# simples de implementar

#Desvantagem
#Ineficiente para faixas grandes de dados 
#Funciona apenas com números inteiros ou discretos
#Consome muita memória se o intervalo for grande