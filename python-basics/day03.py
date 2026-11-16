# 成绩等级判断
print("输入成绩（要求为0-100之间的整数）：")
grade = int(input())
if 0<=grade<=100 :
    if grade >= 90:
        print("优秀")
    elif grade >= 80:
        print("还不错")
    elif grade >= 60:
        print("及格")
    else:
        print("不合格")
else :
    print("数字错误!")

# 闰年判断
print("输入你想判断的年份")
year = int(input())
if year % 4 == 0 and year % 100 !=0 :
    print("是闰年")
elif year % 400 == 0 :
    print("是闰年")
else :
    print("不是闰年")