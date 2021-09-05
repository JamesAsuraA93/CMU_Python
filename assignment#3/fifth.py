def longest_digit_run(n):
    n = str(n)  # "11777888663"
    m = set(n)  # set ที่ไม่ซ้ำ
    lst = list(m)  # list ที่ไม่ซ้ำ   >> [1,7,8,6,3]
    lst_cnt = []  # เก็บค่าจำนวนตัว
    for i in lst:   # [1,7,8,6,3]
        i = str(i)  # วน list  1
        cnt = n.count(i)  # [1,7,8,6,3] >>>>>>v
        lst_cnt.append(cnt)  # ที่เก็บค่าจำนวนตัว  [2,3,3,2,1]
    return max(lst_cnt)   #

