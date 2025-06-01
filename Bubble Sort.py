def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        
        trocou = False
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        if not trocou:
            break
    return lista
lista = [44,90,10,14,5,1]
ordenada = bubble_sort(lista)
print(ordenada)

#Vantagens do Bubble Sort

#Muito fácil de entender e implementar.

#Funciona bem para listas pequenas ou quase ordenadas.

#Estável, ou seja, mantém a ordem relativa de elementos iguais.

#Desvantagens do Bubble Sort

# ineficiente para listas grandes.

#Mesmo otimizado, seu tempo de execução cresce rapidamente com o tamanho da entrada.

