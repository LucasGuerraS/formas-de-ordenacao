def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]  # atribuiçāo paralela


def empurra(lista):
    for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                troca(lista, i , i + 1)


def bubble_sort(lista):
    t = len(lista)
    for i in range(t):
        empurra(lista)

def bubble_sort2(lista):
    t = len(lista)
    while t > 1:
        empurra(lista)
        t -= 1

# main
lista = [40, 30, 20, 50, 10, 55, -10, 1, 4]
bubble_sort(lista)
bubble_sort2(lista)
#duas maneiras de implementar o bubble sort
print(lista)