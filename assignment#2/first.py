def intersects(x1,y1,r1,x2,y2,r2):
    global ans
    d = (((x1-x2)**2) + ((y1-y2)**2))**(0.5)
    detect = d - (r1 + r2)

    if detect > 0:
        ans = -1
    elif detect == 0:
        ans = 0
    elif detect < 0:
        ans = 1
    else:
        pass
    return ans

