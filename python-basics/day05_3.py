# 简易购物清单
Buy_list = []
print("输入您购买的商品(输入q即为结束):")
product = ""
while True:
    product = input()
    if product == "q":break
    else:
        Buy_list.append(product)
print(f"你买了{len(Buy_list)}件:")
for i in Buy_list:
    print(i)