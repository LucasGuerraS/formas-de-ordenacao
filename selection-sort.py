#Selection-sort

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


#MAIN
lista = [-2,-40,430,0,-5,50,32,-222,90,2]
print(f"Lista: {lista}")
print("Ordenando a lista")
print(f"Lista ordenada: {selection_sort(lista)}")
print(lista)