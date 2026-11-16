# 成绩等级判断
print("输入成绩（要求为0-100之间的整数）：")
grade = int(input())
if grade >= 90:
    print(f"优秀")
elif grade >=80:
    print(f"还不错")
elif grade >=60:
    print(f"及格")
else:
    print("不合格")

# 闰年判断
print("输入你想判断的年份")
year = int(input())
if year % 4 == 0 and year % 100 !=0 :
    print("是闰年")
elif year % 400 == 0 :
    print("是闰年")
else :
    print("不是闰年")