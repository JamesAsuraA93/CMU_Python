a, b, c = 2, 5, 3

# 3,1,2
def my_max_mid_min(a, b, c):
    mx = bigger(bigger(a, b), c)  # 3
    mn = smaller(smaller(a, b), c)  # 1
    md = (a + b + c) - (mx + mn)  # 2
    return mx, md, mn  # Tuple passing tuple dont forgot


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def smaller(a, b):
    if a < b:
        return a
    else:
        return b


