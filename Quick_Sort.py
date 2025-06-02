def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]

        return quick_sort(menores) + [pivo] + quick_sort(maiores)

dados = [8, 5, 9, 7, 2, 3, 4]
print(f'lista original:{dados}')
ordenada = quick_sort(dados)
print(f'lista ordenada:{ordenada}')   

#Pontos Positivos

#Muito rápido na prática Mesmo que o pior caso seja O(n²), geralmente ele roda com eficiência O(n log n).

#In-place Não precisa de muita memória extra — reorganiza na própria lista.

#Bom para grandes volumes de dados É um dos mais usados em bibliotecas e sistemas reais.

# Pontos Negativos

#Não é estável Elementos iguais podem trocar de posição.

#Pior caso é ruim (O(n²)) Pode acontecer se escolher sempre o pior pivô (por exemplo, o menor ou maior número da lista).

#Mais complexo de implementar que Bubble ou Insertion Usa recursão e manipulação de índices com mais cuidado.