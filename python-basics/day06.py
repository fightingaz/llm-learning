li1 = ["apple", "banana", "apple", "watermelon", "grape"]
for num1,fruit in enumerate(li1,start=1):
    print(f"{num1}. {fruit}")
while True:
    print("输入你想删除的编号：")
    num = int(input())
    if num == 0:
        print("退出清单")
        break
    if 0 < num <= len(li1):
        li1.pop(num-1)
        for num1, fruit in enumerate(li1, start=1):
            print(f"{num1}. {fruit}")
    else:
        print("没有这个编号请重新输入")


