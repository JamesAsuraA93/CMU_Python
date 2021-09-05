def bin_flt(flt):  # "534"
    flt = float("0." + flt)  # float("0.534") >> 0.534
    temp = ""
    for i in range(6):
        flt *= 2  # 0.534 * 2  >> 1.068  ,  0.068 * 2 >> 0.136 > 0.272 0.544 1.088
        temp += str(int(flt))  # str(int(0.136))  >> str(0) >> '0' , temp += '0' >> temp = "100010"
        if flt >= 1:  # 1.068 >= 1
            flt -= 1  # 1.068 - 1 = 0.068
    return temp  # "100010"


def bin_dem(dem):
    return bin(int(dem)).replace("0b", "")  # bin(35) >> "100011"


def float_to_bin(number):
    number = float(number)
    dem, flt = str(number).split(".") # "35.534".split(".") => ["35","534"]

    dem = bin_dem(dem)  # "100011"
    flt = bin_flt(flt)  # "100010"
    return dem + "." + flt


print(float_to_bin(35.534))