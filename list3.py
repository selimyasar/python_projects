liste = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(x):
    sonuc = []
    for i in x:
        sonuc = [i] + sonuc
    return sonuc

reverse_list(liste)

print(reverse_list(liste))