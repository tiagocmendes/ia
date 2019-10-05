# 4.1
odd = lambda n: n % 2 != 0

# 4.2
positive = lambda n: n > 0

# 4.3
module = lambda x,y: abs(x) < abs(y)

# 4.4
import math
polar = lambda x, y: (math.sqrt(x*x + y*y), math.atan2(y,x))

# 4.5
def exerc4_5(f,g,h):
    return lambda x, y, z: h(f(x,y), g(y,z))

nova = exerc4_5(lambda a, b: a+b, lambda a, b: a*b, lambda a, b: a < b)

# 4.6
quantificador_universal = lambda l,f: True if l == [] else f(l[0]) and quantificador_universal(l[1:], f)
    # return not False in [f(e) for e in l]
    #return l == [e for e in l if f(e)]

# 4.7
quantificador_existencial = lambda l, f: False if l == [] else f(l[0]) or quantificador_existencial(l[1:], f)

# 4.8
subset = lambda l1, l2: True if l1 == [] else l1[0] in l2 and subset(l1[1:], l2)

# 4.9


if __name__ == "__main__":

    print("{} % 0 == 0? {}".format(2,odd(2)))
    print("{} % 0 == 0? {}".format(3,odd(3)))
    print("{} > 0 ? {}".format(1,positive(1)))
    print("{} > 0 ? {}".format(0,positive(0)))
    print("{} > 0 ? {}".format(-1,positive(-1)))
    print("|{}| < |{}|? {}".format(1,2,module(1,2)))
    print("|{}| < |{}|? {}".format(-4,2,module(-4,2)))
    print("Polar de ({},{})? {}".format(2,1,polar(2,1,)))
    print("Quantificador universal: {} > 0? {}".format([1,2,3,-4,5],quantificador_universal([1,2,3,-4,5], positive)))
    print("Quantificador existencial: {} > 0? {}".format([-1,-2,-3], quantificador_existencial([-1,-2,-3], positive)))
    print("Quantificador existencial: {} > 0? {}".format([-1,-2,-3], quantificador_existencial([-1,2,-3], positive)))
    print("Subconjunto: {} C {}? {}".format([1,2,3],[1,2,3,4,5,6], subset([1,2,3],[1,2,3,4,5,6])))
    print("Subconjunto: {} C {}? {}".format([1,2,3],[1,2,4,5,6], subset([1,2,3],[1,2,4,5,6])))
