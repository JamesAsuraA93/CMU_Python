def round_to_int(x):
    if x > 0:
        x += 0.49999999999999999999999999999999999
        return int(x)
    elif x < 0:
        x += -0.49999999999999999999999999999999999
        return int(x)
    else:
        return 0
