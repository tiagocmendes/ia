import sys 

# 1.1
def list_length(l):
    if l == []:
        return 0
    return 1 + list_length(l[1:])

# 1.2
def list_sum(l):
    if l == []:
        return 0
    try:
        return l[0] + list_sum(l[1:])
    except TypeError as typeError:
        print("TypeError: {}".format(typeError))
        sys.exit(1)

# 1.3 
def check_elem(elem, l):
    if l == []:
        return False
    return elem == l[0] or check_elem(elem, l[1:]) 

# 1.4
def concatenation(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    l1.append(l2[0])
    return concatenation(l1, l2[1:])
    
# 1.5
def inverse(l):
    if l == []:
        return []
    return inverse(l[1:]) + [l[0]]

# 1.6
def capicua(l):
    if l == [] or len(l) == 1:
        return True
    return l[0] == l[-1] and capicua(l[1:-1])

# 1.7
def list_concatenation(l):
    return concatenation(l[0][:], l[1][:])

# 1.8
def exchange(l,x,y):
    if l == []:
        return []
    return [y if l[0] == x else l[0]] + exchange(l[1:],x,y)

if __name__ == '__main__':
    my_list = [1,2,3,4,5]
    print("\nList: {}\n".format(my_list))

    # exercises
    ex1_1 = list_length(my_list)
    ex1_2 = list_sum(my_list)
    ex1_3 = check_elem(5, my_list)
    ex1_4 = concatenation([1,2,3,4,5],my_list)
    ex1_5 = inverse(my_list)
    ex1_6 = capicua(my_list)
    ex1_7 = list_concatenation([my_list, [1,2,3,4,5]])
    ex1_8 = exchange(my_list + [2,2,2,2],2,69)

    print("1.1 - Length = {}".format(ex1_1))
    print("1.2 - Sum = {}".format(ex1_2))
    print("1.3 - 5 is {} in list".format("" if ex1_3 else "not"))
    print("1.4 - Concatenation = {}".format(ex1_4))
    print("1.5 - Inverse = {}".format(ex1_5))
    print("1.6 - Capicua = {}".format(ex1_6))
    print("1.7 - List Concatenation = {}".format(ex1_7))
    print("1.8 - Exchange = {}".format(ex1_8))