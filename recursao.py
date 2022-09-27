def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


def soma_itens_rtecursivo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_itens_rtecursivo(lista[1:])


# principal
print(soma_lista([1, 3, 4, 7, 9]))
print(soma_itens_rtecursivo([1, 3, 4, 7, 9]))
