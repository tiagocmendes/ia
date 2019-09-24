# 2.1
def separa(l):
    if l == []:
        return [], []
    
    a, b = l[0]
    la, lb = separa(l[1:])
    return [a] + la, [b] + lb

# 2.2
def remove_e_conta(l, elem):
    if l == []:
        return [], 0
    
    r, c = remove_e_conta(l[1:], elem)
    if l[0] == elem:
        return r, c+1
    else:
        return [l[0]] + r, c

if __name__ == '__main__':

    l = [(1,2),(3,4), (5,6), (7,8)]
    a = separa(l)
    b = remove_e_conta([1,6,2,5,5,2,5,2], 2)
    print(a)
    print(b)