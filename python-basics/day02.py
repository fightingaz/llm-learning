# 温度转换器
print("这是一个温度转换器,将摄氏度转换成华氏度")
print("input a number:")
celsius = float(input())   # input的返回值永远是字符串str'''
print(f"对应的华氏度为：{celsius*1.8+32}")

# BMI计算器
print("这是一个BMI计算器")
print("input your weight:")
weight = float(input())
print("input your height:")
height = float(input())
print(f"你的BMI为：{weight/(height*height)}")

# 简单计算器
print("这是一个简单的计算器")
print("input your numer1:")
number1 = float(input())
print("input your numer2:")
number2 = float(input())
print("输入你想要的计算符号")
cal = input()
if(cal == '+'):
    print(f"{number1+number2}")
elif(cal == '-'):
    print(f"{number1-number2}")
elif(cal == '*'):
    print(f"{number1*number2}")
elif(cal == '/'):
    print(f"{number1/number2}")