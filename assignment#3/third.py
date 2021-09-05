def prime(x):
    m = x // 2
    for i in range(2, m + 1):
        if x % i == 0:
            return False
    return True


def compo(x):
    lst = []
    keep = x
    start = 2
    while x != 1:
        if x % start != 0:
            start += 1
            if start % 2 == 0 and start != 2:
                start += 1
        x //= start
        lst.append(start)

    com = str(lst)[1:-1].replace(",", " *")

    say = f"{keep} is " + com
    return say


def factorize(x):
    if x == 0:
        return f"{x} is 0"
    elif x == 1:
        return f"{x} is 1"
    if x > 1 and prime(x):
        return f"{x} is prime"

    elif x > 1 and (prime(x) == False):
        say = compo(x)
        return say
