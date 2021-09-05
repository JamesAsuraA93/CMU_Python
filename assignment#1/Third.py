def calculate_p2p_evolve_exp(p,c):
    evole = 0
    for i in range(p):
        if c-12>=0:
            c -= 12
            evole += 1
            c+=1
        else:
            pass
    return 500*evole

print(calculate_p2p_evolve_exp(3,33))
