flat_list = []

def flatten_list(x):
    for i in x:
        if i == list:
            flatten_list(i)
        else:
            reversed(liste)
    return flat_list

liste = [[1, 2], [3, 4], [5, 6, 7]]
print('Orjinal Liste', liste)
print('Düzeltilmiş liste',flatten_list(liste))
