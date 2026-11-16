import random

# 九九乘法表
for i in range(1,10):
    j = 1
    while i>=0 :
        print(f"{i}*{j}={i*j}",end=" ") # end参数用来设置输出的结尾,print函数默认会换行
        if j == i :
            print(""),
            break
        j += 1
    i+=1

# 猜数字游戏
a = random.randint(1,100)
print("猜一个1到100之间的整数（包括1和100）")
b = int(input())
if a == b :
    print("you are right!")
else :
    print("you are wrong!")
    print(f"the number is {a}")
