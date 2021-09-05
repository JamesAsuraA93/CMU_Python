def big(a,b):
    if a>b:
        return a
    else:
        return b

def small(a,b):
    if a<b:
        return a
    else:
        return b

def is_p_triple(a,b,c):
    min = small(small(a,b),c)
    max = big(big(a,b),c)
    mid = (a+b+c) - (max+min)
    if max**2 == (min**2) + (mid**2):
        return True
    else:
        return False
