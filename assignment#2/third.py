# 13 4

# เพิ่มวันพิเศษเข้าไปในเดือนกุมภาพันธ์ในปีที่หารด้วย 4 ลงตัว
# ยกเว้นปีที่หารด้วย 100 ลงตัวและหารด้วย 900 แล้วไม่เหลือเศษเป็น 200 หรือ 600
days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def extra(y):
    if y%4==0 and (y%100!=0 or (y%900 == 200 or y%900 == 600 )):
        return 1
    else:
        return 0

def count_down_to_songkran(d,m,y):
    fig_days = 13
    if m < 4:
        ans = ((sum(days_of_month[m-1:3])) - d) + fig_days + (extra(y))
        return ans
    elif m == 4:
        ans = fig_days - d
        return ans
    else:
        pass

