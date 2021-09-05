def is_overlapped(x1,y1,w1,h1,x2,y2,w2,h2):
    return False if (((x1) - (x2+w2) > 0) or ((y2)-(y2+h2) > 0) or ((x2)-(x1+w1)) > 0 or ((y2)-(y1+h1)) > 0) else True

