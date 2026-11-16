import random

# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1) : # range函数会自动控制变量的变化
        print(f"{i}*{j}={i*j}",end=" ") # end参数用来设置输出的结尾,print函数默认会换行
    print("")

# 猜数字游戏
a = random.randint(1,100)
print("猜一个1到100之间的整数（包括1和100）")
while 1 :
    b = int(input())
    if b==a :
        print("you are right!")
        break
    else:
        print("you are wrong!")