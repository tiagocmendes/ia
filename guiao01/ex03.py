import list_sum from ex01

# 3.1
def head(l):
    if l == []:
        return None 
    return l[0]

# 3.2
def tail(l):
    if len(l) < 2:
        return None
    return l[1:]

# 3.3
def juntar(l1, l2):
    if len(l1) != len(l2):
        return None
    if l1 == []:
        return []
    
    return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

# 3.4
def min_element(l):
    if l == []:
        return None
    mini = min_element(l[1:])
    if mini == None or l[0] < mini:
        return l[0]
    else:
        return mini

# 3.5
def remainder(l):
    if l == []:
        return None 
    res = remainder(l[1:])
    if res == None:
        return [l[0], l[1:]]
    elif l[0] < res[0]: 
        return [l[0], [res[0]] + res[1]]
    else:
        return [res[0], res[1] + [l[0]]]

# 3.6
def min_and_max(l):
    if l == []:
        return None
        
    res = min_and_max(l[1:])
    
    if res == None:
        return l[0], l[0]

    mini, maxi = l[0], l[0]
    if res[0] < mini:
        mini = res[0]
    if res[1] > maxi:
        maxi = res[1]
    
    return mini, maxi

# 3.7
def lower_two(l):
    fst_min, re = remainder(l)
    snd_min, re = remainder(re)
    return fst_min, snd_min, re

if __name__ == "__main__":
    a = head([])
    b = head([1,2,3])
    c = tail([]) 
    d = tail([1,2,3])
    e = tail([1])
    f = juntar([1,2,3],[3,4,5])
    g = min_element([])
    h = min_element([3,4,6,1,-2,5])
    i = remainder([3,-4,1,2,1,5])
    j,k = min_and_max([1,2,5,12,6,-12,841,63])
    l, m, n = lower_two([1,2,5,12,6,-12,841,63])

    print(f"Cabeça de []: {a}")
    print(f"Cabeça de []: {b}")
    print(f"Cauda de []: {c}")
    print(f"Cauda de []: {d}")
    print(f"Cauda de []: {e}")
    print(f"Juntar: {f}")
    print(f"Minimo: {g}")
    print(f"Minimo: {h}")
    print(f"Remainder: {i}")
    print(f"Minimum: {j}, Maximum: {k}")
    print(f"First min: {l}, Second min: {m}, Remainder: {n}")