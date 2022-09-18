reserve_list = []

def reserve(x):
    for i in x:
        if type(i) == list:
            reserve(i)
        else:
            reserve_list.reverse(i)
        return reserve_list    