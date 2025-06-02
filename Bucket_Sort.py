def bucket_sort(lista):
    tamanho = len(lista)
    buckets = [[] for _ in range(tamanho)]

    
    for valor in lista:
        indice = int(valor * tamanho)
        buckets[indice].append(valor)

    
    for i in range(tamanho):
        buckets[i].sort()

   
    resultado = []
    for balde in buckets:
        resultado.extend(balde)

    return resultado


dados = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Original:", dados)
ordenada = bucket_sort(dados)
print("Ordenada:", ordenada)

#Pontos Positivos

#Muito rápido quando os dados são bem distribuídos.

#Bom para números decimais ou dados contínuos.

#Estável, se o sort interno for estável.


#Pontos Negativos

#Requer conhecimento da distribuição dos dados 
# Se os dados forem mal distribuídos, ele perde eficiência.

#Consome memória com muitos baldes

#Desempenho depende do sort interno em cada balde