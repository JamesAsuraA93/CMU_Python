def love6(first, second):
    if (first or second) and first + second == 6 and (first - second == 6 or second - first == 6):
        return True
    else:
        return False
