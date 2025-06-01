def counting_sort_by_digit(arr, digit_place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  

    
    for num in arr:
        digit = (num // digit_place) % 10
        count[digit] += 1

    
    for i in range(1, 10):
        count[i] += count[i - 1]

    
    for num in reversed(arr):
        digit = (num // digit_place) % 10
        count[digit] -= 1
        output[count[digit]] = num

    return output

def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    digit_place = 1

    while max_num // digit_place > 0:
        arr = counting_sort_by_digit(arr, digit_place)
        digit_place *= 10

    return arr


nums = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(nums))
























#Vantagens:
#Excelente desempenho com grandes volumes de dados numéricos

#Tempo linear quando d e k são pequenos

#Estável (mantém a ordem dos elementos com valores iguais)

#Desvantagens:
#Só funciona com inteiros ou strings com tamanho fixo

#Requer espaço extra para arrays auxiliares

#Pode ser menos eficiente se os números tiverem muitos dígitos

