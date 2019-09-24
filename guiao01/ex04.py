# 4.1
odd = lambda n: n % 2 != 0

# 4.2
positive = lambda n: n > 0

# 4.3
module = lambda x,y: abs(x) < abs(y)

# 4.4
import math
polar = lambda x, y: (math.sqrt(x*x,y*y), math.atan2(y,x))

# 4.5
def exerc4_5(f,g,h):
    return lambda x, y, z: h((f,y), g(y,z))

nova = exerc4_5(lambda a, b: a+b, lambda a, b: a*b, lambda a, b: a < b)

def quantificador_universal(l,f):
    # return not False in [f(e) for e in l]
    return l == [e for e in l if f(e)]

if __name__ == "__main__":

    print("{} % 0 == 0? {}".format(2,odd(2)))
    print("{} % 0 == 0? {}".format(3,odd(3)))
    print("{} > 0 ? {}".format(1,positive(1)))
    print("{} > 0 ? {}".format(0,positive(0)))
    print("{} > 0 ? {}".format(-1,positive(-1)))
    print("|{}| < |{}|? {}".format(1,2,module(1,2)))
    print("|{}| < |{}|? {}".format(-4,2,module(-4,2)))
