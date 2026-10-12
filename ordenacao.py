def quick_sort(valores):
    if len(valores) <= 1:
        return valores

    pivot = valores[len(valores) // 2]

    menores = []
    iguais = []
    maiores = []

    for valor in valores:
        if valor < pivot:
            menores.append(valor)
        elif valor == pivot:
            iguais.append(valor)
        elif valor > pivot:
            maiores.append(valor)
    return quick_sort(menores) + iguais + quick_sort(maiores)
print(quick_sort([7, 3, 9, 1, 5]))

