# 3.3
def juntar(l1, l2):
    if len(l1) != len(l2):
        return None
    if l1 == []:
        return []
    
    return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

if __name__ == "__main__":
    a = juntar([1,2,3],[3,4,5])
    print(a)