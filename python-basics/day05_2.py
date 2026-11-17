# 筛选偶数
li1 = [12,2,3,4,5,6]
for i in li1:
    if i % 2 == 0:
        print(i)
    if i > 10 and i % 2 != 0:
        print(i)

# 成绩+等级
li2 = [50,60,70,80,90,110]
for i in li2:
    if 0<=i<=100:
        if i >= 90:
            print(f"{i}->优秀")
        elif i >= 80:
            print(f"{i}->还不错")
        elif i >= 60:
            print(f"{i}->及格")
        else:
            print(f"{i}->不合格")
    else:
        print("成绩错误")
