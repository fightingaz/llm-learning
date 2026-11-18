# 水果仓库
li1 = ["apple", "banana", "cherry", "watermelon", "grape"]
for i in li1:
    print(i)
print(li1[0])
print(li1[2])
print(len(li1))
for i in range(len(li1)): # range函数如果不设置起点则默认从0开始
    print(f"{i+1}.",li1[i])

# 算平均分
li2 = []
print("输入三个数字:")
for i in range(1,4): # range函数包前不包后
    li2.append(float(input()))
print(f"总分为{sum(li2)}")
print(f"平均分为{sum(li2)/len(li2)}")

# 找最高分
li3 = []
print("输入五个成绩：")
for i in range(1,6):
    li3.append(float(input()))
highest = li3[0]
for i in li3:
    if i > highest:
        highest = i
print(highest)
