def bubble(the_list):
    rng = len(the_list)
    chk = rng
    for time in range(rng):
        for j in range(0, chk - 1):
            if the_list[j] < the_list[j + 1]:
                temp = the_list[j]
                the_list[j] = the_list[j + 1]
                the_list[j + 1] = temp
            else:
                pass
        chk -= 1
    return the_list


n = int(input("Total students: "))
print("Enter score:\r")
lst = []
for i in range(n):
    score = int(input())
    lst.append(score)

print(bubble(lst))

TheSet = set(lst)
Runlst = list(TheSet)  # ลบตัวซ้ำ Runner Up
Max = format(bubble(lst)[0], ".2f")
if len(Runlst) == 1:
    Run = "None"
else:
    Run = format(bubble(Runlst)[1], ".2f")
Avg = format(sum(lst) / n, ".2f")

print(
f"""
Max score is: {Max}
Runner up is: {Run}
Average is: {Avg}
""")
