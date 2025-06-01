lista = [64, 25, 12, 22, 11]

def selection_sort(lista):
    n= len(lista)
    for i in range(n):
        
        menor_elemento = i
        
        for j in range(i+1, n):
            if lista[j] < lista[menor_elemento]:
                menor_elemento = j
        
        lista[i],lista[menor_elemento] = lista[menor_elemento], lista[i]
    return lista



ordenada = selection_sort(lista)
print(ordenada)

# Vantagem 
# Simplicidade, não necessita de memoria extra  

#Desvantagem

# não é estavel
# ineficiente em listra grandes
# faz comparaçoes desnecessarias mesmo a lista ja estando ordenada