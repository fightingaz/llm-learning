# 成绩单
dic = {"语文": 90,"数学": 85, "英语": 78}
sum1 = 0
for i in dic.values():
    sum1 += i
print(f"总分为{sum1}")
print(f"平均分为{sum1/len(dic):.1f}")
max1 = 0
max2 = ""
for k,v in dic.items():
    if v > max1:
        max1 = v
        max2 = k
print(f"最高分{max1},对应科目为{max2}")
