

# Python是一种面向对象的解释型高级编程语言

编译性语言和解释性语言是两种不同的程序语言执行方式，它们在源代码转换成机器码的过程中有着本质的区别。

### 编译性语言

编译性语言，如**C、C++和Pascal**，需要通过编译器将源代码一次性转换成机器语言，生成可执行文件（例如Windows下的.exe文件）。这种转换只需进行一次，之后就可以无限次运行生成的机器码，无需再次编译。编译性语言的优势在于执行效率高，但由于依赖于编译器，它们通常**不具备良好的跨平台性**。不同的操作系统可能需要不同的编译器，而且可执行文件通常无法在不同的操作系统间移植。

### 解释性语言

解释性语言，如**Python、JavaScript和Ruby**，不需要预先编译。源代码在**程序运行时由解释器逐行转换成机器语言**。这意味着每次执行程序时，源代码都需要被重新解释，这通常会导致解释性语言的执行效率低于编译性语言。然而，解释性语言的优势在于跨平台性好，因为不同平台的解释器可以将相同的源代码解释成适合该平台的机器码。

### Java的特殊性

Java语言是一种特殊的情况，它结合了编译性和解释性语言的特点。**Java源代码首先被编译成与平台无关的字节码文件（.class文件），然后这些字节码文件可以在不同平台的Java虚拟机（JVM）上运行。JVM在运行时解释字节码，这个过程是解释性的**。

### 总结

编译性语言和解释性语言各有优缺点。编译性语言在执行效率上通常更胜一筹，但跨平台性较差。解释性语言虽然执行效率不如编译性语言，但在跨平台性上表现更佳。选择使用哪种语言往往取决于项目的具体需求和目标平台。

### Python是强类型的脚本语言

# Debug的使用

![image-20250408113905258](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250408113905258.png)

1. 蓝色代码为下一条将要执行的代码
2. 在代码左侧点击即为设置断点
3. Show Execution Point 为显示当前执行的断点
4. run to cursor为执行到下一个断点
5. step into是执行下一条代码

# 注释

## 单行注释（#+空格）

```python
print(123)
# print(123)
print(123)
```

## 多行注释（三个单引号或双引号）

```python
print(123)
'''
print(123)
print(321)
'''
```

# print函数

## values

一次可以输出多个值，但是多个值之间必须要用逗号隔开，否则会被当成一个值输出

```python
print("wuhu""qifei")
print("wuhu","qifei")
```

## sep

用来设置多个值之间的分隔符，默认为空格

```python
print("wuhu""qifei")
print("wuhu","qifei")
print("wuhu","qifei",sep="=")
```

## end

输出值的结尾，默认是换行符'/d'，可以自己改成字母、符号或数字。

```python
print("wuhu""qifei")
print("wuhu","qifei")
print("wuhu","qifei",sep="=")
print("wuhu","qifei",sep="=",end="2")
```

# 定义变量

直接  ***变量 = 值***

```python
num1 = 1
num2 = 2
total =num1 + num2
```

变量在赋值以后才会被创建，与Java和c不同，不能直接定义一个某种类型的变量。

# 标识符

1. 只能由数字、字母、下划线组成
2. 不能用数字开头
3. 不能是关键字
4. 严格区分大小写

# 数值类型

可以用type()函数来获取一个变量的数据类型

```python
num1 = 1
num2 = 2
total =num1 + num2
print(type(total))
```

1. int

2. bool

3. float

4. complex（复数） a+bj  

   

# 字符串类型

```python
name1 = 'hello'
name2 = "world"
name3 = """monster
hunter"""
```

上述三种都是定义字符串，当三引号前面没有变量名时，就是多行注释的效果

# 格式化输出

```python
name = "xiebowen"
age = 18
print("my name is %s,my age is %d"%(name,age))
```

%s是输出字符串，%d是输出数字。%6d是输出6位的数字，前面不足会用空白补全，若超出则按原样输出。

%06d是将空白换成0，用0来补全。

```python
money = 1.234
print("%f"%money)
print("%.7f"%money)
```

%f输出一个浮点数，默认有六位小数，不足时用0补全。

%.7f设置为七位小数，不足时用0补全。

```python
print("wode%%shi%%"%())
```

输出单个百分号

```python
age = 18
name = "xiebowen"
print(f"我的名字是{name},我的年龄是{age}")
```

**在要输出的内容前面加个f，要输出的变量外加个花括号**

# 算术运算符

```python
num1 = 1
num2 = 2
a = num2/num1
print(num2/num1)
print(type(a))
```

使用除法运算时，得到的商一定是浮点数，且除数不为0

```py
a = 10
b = 3
c = a%b
d = a//b
print(c)
print(d)
print(a**b)
```

%是取模（取余数），//是取整数 ，a**b是a的b次方

参加运算的数中若有浮点数，那么最终的结果也会是浮点数

# input函数

```python
pwd = input("请输入密码：")
print(pwd)
```

input()直接获取你控制台的输入，默认是字符串类型

# 转义字符

```python
print("a\tb\tc\td\te")
print("a\nb\nc\nd\ne")
print("a\rb\rc\rd\re")
print("abcd\\e") 
print(r"abcd\\e")
```

\t是四个空白字符，\n是换行字符，\r是回到当前行的开头并输出（可能会覆盖掉原有内容），双 \ 就是输出一个 \ 。

在字符串前面加个r表示字符串内部不进行转义。

# 逻辑运算符

1. and就是与  都为真才真
2. or就是或   有一个为真就是真
3. not就是非   就是取反

# if、elif、else

## if选择

```python
s=input("请输入你的成绩：")
score=int(s)
if 90<=score<=100:
    print("优秀")
elif 80<=score<90:
    print("不错")
elif 60<=score<80:
    print("及格")
else:
    print("回家吧")
```

## if嵌套

```python
money=int(input("请输入你的余额："))
ticket=9
if ticket>0:
    if money>0:
        print("你可以购买该车票")
    else:
        print("你的钱不够买票的")
else:
    print("没车票了")
```

# while

## 循环

```typescript
i=int(input("请输入您想要的数字："))
sum=i
while i>0:
    i-=1
    sum+=i
print("%d"%sum)
```

## 嵌套

```python
i=int(input("请输入您想要的数字："))
sum=i
j=3
while i>0:
    i-=1
    sum+=i
    print("我是外循环")
    while j>0:
        j-=1
        print("我是内循环")
print("%d"%sum)
print("%d"%j)
```

# for

```python
str=input("请输入一个字符串：")
for i in str:
    print(i)
```

遍历str字符串

# range函数

```python
for i in range(1,9):
    print(i)
```

range相当于一个计数器，确定循环次数。

若指定两个参数，则代表指定了起始位置和结束位置。

（1，9）可理解为数学中的【1,9）。遵循包前不包后原则。

i 的值从1开始，到9结束，且不包括9.

```python
for i in range(9):
    print(i)
```

若只指定一个参数，那就代表该参数为循环次数，i 的值默认从0开始。

# break和continue关键字

```python
for i in range(1,10):
    if i==7:
        continue
    if i==8:
        break
    print(i)
```

continue是结束当前这次循环，继续下次循环。

break是结束这个循环，跳出循环。

# 字符串编码

本质上就是二进制数据与语言文字的一 一对应关系。

1. Unicode编码中，所有字符就是两个字节。优点是字符与数字之间转换速度更快，缺点是占用空间大。
2. UTF-8是对不同的字符用不同的长度表示。优点是占用空间小，缺点是字符与数字之间转换速度更快。

```python
str=input("你想说什么：")
a1=str.encode()
print(a1,type(a1))
a2=a1.decode("utf-8")
print(a2,type(a2))
```

encode()就是将字符串转换为二进制数据，decode()就是将二进制数据按指定编码方式转换为字符串。

# 字符串常见操作

## 字符串拼接(利用+号)

```python
str1=input("str1=")
str2=input("str2=")
print("拼接结果为：",str1+str2)
```

## 字符串重复输出(*+要重复输出的次数)

```python
str1=input("str1=")
str2=input("str2=")
print("拼接结果为：",(str1+str2)*5)
```

## 成员运算符 （检查字符串中是否包含某子串）

### in(包含)和not  in(不包含) 

```python
str="aaabbb"
print("a" in str)
print("b" in str)
print("c" in str)
print("c" not in str)
```

## 下标

```python
str="jinitaimei"
print(str[0])
print(str[-1])
```

字符串下标从左往右数是从0开始，从右往左数是从-1开始，这样可以轻易找到第n个元素位置和倒数第n个元素位置。

## 切片（截取子字符串）

```python
str="jinitaimei"
print(str[:4])
print(str[2:4])
print(str[7:])
print(str[7:-1])
print(str[:-1])
print(str[-1:])
print(str[-1::-1])
```

str[起始位置：结束位置：步长]

同样遵循包前不包后原则，不会包含结束位置的元素。当结束位置为空时，python会默认截取剩下的所有元素

当起始位置为空时，默认从下标为0开始截取。

步长的绝对值大小决定截取的间隔，正负号则决定截取的方向。正数表示从左往右截取，负数表示从右往左截取。

将步长设置为1，起始位置设置为-1，结束位置为空则可以实现将字符串倒置。

## 查找子字符串位置

### find("要找的子字符串"，起始位置，结束位置)

```python
str="jinitaimei"
print(str.find("mei"))
print(str.find("mei",1,3))
```

同样遵循包前不包后原则，不会找到结束位置的字符。

若不指定起始位置和结束位置则表明在整个字符串中查找。

若在指定范围中没有查找到该子字符串则会返回-1。

### index("要找的子字符串"，起始位置，结束位置)

```python
str="jinitaimei"
print(str.index("mei"))
print(str.index("mei",1,3))
```



同样遵循包前不包后原则，不会找到结束位置的字符。

若不指定起始位置和结束位置则表明在整个字符串中查找。

**若在指定范围中没有查找到该子字符串则报错。**（与find的区别）

## 获取子字符串在字符串中出现次数

```python
str="jinitaimei"
print(str.count("mei"))
print(str.count("mei",1,3))
```

同样遵循包前不包后原则，不会找到结束位置的字符。

若不指定起始位置和结束位置则表明在整个字符串中查找。

## 判断字符串某位置是否以指定字符串开头或结尾

```python
str="jinitaimei"
print(str.startswith("mei"))
print(str.startswith("mei",1,3))
```

```python
str="jinitaimei"
print(str.endswith("mei"))
print(str.endswith("mei",1,3))
```

## 判断字符串中所有字母是否都为大写

```python
str="jinitaimei"
print(str.isupper())
```

## 修改元素

```python
str="jinitaimei"
print(str.replace("i","a",1))
print(str.replace("i","a",2))
print(str.replace("i","a",4))
```

replace(旧内容，新内容，替换次数)

## 指定分隔符来切字符串

```python
str="jini,taimei"
print(str.split(",",1))
print(str.split("n",1))
print(str.split("i",1))
print(str.split("i",2))
print(str.split("i",4))
```

以指定的分隔符来切开字符串，并以列表的形式输出，指定的分隔符不会被输出

## 第一个字符大写，其它都小写

```python
str="jini,Taimei"
print(str.capitalize())
```

## 字符串大小写转换

```python
str="jini,Taimei"
print(str.lower())
print(str.upper())
```

# 列表相关操作

```python
li = [1,2,3,4]
for i in li:
    print(i)
print(li[1:3])
```

列表是可迭代对象，可以用for循环遍历，也可以像字符串一样进行切片操作

## 添加元素

```python
li = [1,2,3,4]
for i in li:
    print(i)
print(li[1:3])
li.append(5)
print(li)
li.extend("1234")
print(li)
li.insert(2,99)
print(li)
```

1. append是将整个对象添加进列表
2. extend是将对象拆分成一个一个的元素再添加进去，只适用于要加进去的对象是可迭代对象，如字符串
3. insert是在指定位置插入指定对象，插入后原有元素会自动后移

## 修改元素

```python
li = [1,2,3,4]
li[0]=9
print(li)
```

## 查找元素

```python
li=["谢德萱","吴灿","罗明珠"]
while 1:
    id = input("请输入你的姓名：")
    if id in li:
        print(f"{id}已存在")
    else:
        print(f"{id}可用")
        li.append(id)
        break
        print(f"您的昵称：{id}注册成功")
print(li)
```

列表和字符串一样都是可迭代对象，可以使用 in 或 not in 来判断列表或字符串中是否存在某元素

```python
li=["谢德萱","吴灿","罗明珠"]
print(li.index("谢德萱"))
print(li.count("吴灿"))
```

index方法返回查找元素的下标，count方法返回查找元素的列表中的个数。

## 删除元素

```python
li=["谢德萱","吴灿","罗明珠"]
li.remove("谢德萱")
print(li)
li.pop(0)
print(li)
del li
```

remove是删除指定元素。

pop是删除指定下标元素，不指定的话默认删除最后一个元素。

del是删除列表

## 排序

```python
li=["谢德萱","吴灿","罗明珠"]
li.sort()
print(li)
li.reverse()
print(li)
```

sort方法默认将列表按从小到大的顺序排列1，reverse方法是将列表倒置。

## 列表推导式

```python
li=[]
[li.append(i) for i in range(1,6)]
print(li)
```

格式一：[表达式 for 变量 in 列表]      in后面不仅可以放列表，还可以放range(),可迭代对象

```python
li=[]
[li.append(i) for i in range(1,6) if i%2!=0]
print(li)
```

格式二：[表达式 for 变量 in 列表 if 条件]

## 列表嵌套

```python
li=[1,2,3,[4,5,6]]
print(li[3])
print(li[3][2])
```

列表中的列表可以被当成元素取出，也可以当成一个列表取出其内部元素。li[3]此时就是一个列表。

# 元组（tuple）

```python
tua=(1,2,3,4)
print(type(tua))
tub=()         # 定义空元组
print(type(tub))
tuc=(1)
print(type(tuc))
tud=(1,)
print(type(tud))
```

当括号内只有一个元素的时候，会默认是该元素的数据类型，如果加个逗号，那么就会变成元组。

元组只能通过下标进行查询操作，不支持增删改操作。

# 字典(dict)

```python
dic={"name":"谢德萱","age":18}
print(dic)
print(type(dic))
dic2={"name":"谢博文","name":20}
print(dic2)
```

字典由键值对组成，键具有唯一性，键名重复不会报错，但是后面的值会覆盖掉前面的值

## 查看元素

```py
dic={"name":"谢德萱","age":18}
print(dic)
print(type(dic))
dic2={"name":"谢博文","name":20}
print(dic2)
print(dic2["name"])
```

可以通过   字典名[键名]  的方式来查看字典内的元素。

## 修改元素

```python
dic={"name":"谢德萱","age":18}
dic["age"]=20
print(dic)
```

注意：键名若存在，则会修改键名的值。若键名不存在，则会新增键。

```python
dic={"name":"谢德萱","age":18}
dic["age"]=20
print(dic)
dic["length"]=160
print(dic)
```

## 删除元素

```python
dic={"name":"谢德萱","age":18}
dic["age"]=20
print(dic)
dic["length"]=160
del dic['age']  #删除字典内的键值对
print(dic)
dic.clear()  #清空字典内的数据，保留字典
print(dic)
dic.pop("name")   #删除指定的键值对
print(dic)
del dic  #删除整个字典
```

## len()求长度

```python
dic={"name":"谢德萱","age":18}
print(len(dic))
```

返回目标对象的长度

## keys()返回键名

```python
dic={"name":"谢德萱","age":18}
print(dic.keys())
```

## items()返回字典内的键值对并以元组形式

```python
dic={"name":"谢德萱","age":18}
for i in dic.items():
    print(i)
```

# 集合

集合具有无序性，输出时会按照hash表排列后再输出。因为Python中int整型的hash值就是它本身，而字符串类型的hash值是会改变的，输出时按hash值从小到大排列。所以最后数字的顺序是按从小到大排列，而字符串则随机。

```python
s1={'a','b','c','d','e','f'}
print(s1)
s2={1,2,3,4,5}
print(s2)
```

集合具有唯一性，会自动去除内部的重复元素

```python
s2={1,2,3,4,5,8,8,8}
print(s2)
```

## 添加元素

```python
s2={1,2,3,4,5,8,8,8}
s2.add(9)       # 添加单个元素
print(s2)
s2.update((10,11,12))    # 将传入的元素拆分，一个个加入集合中
print(s2)
```

## 删除元素

```python
s2={1,2,3,4,5,8,8,8}
s2.add(9)
print(s2)
s2.update((10,11,12))
print(s2)
s2.remove(9)  # 删除指定元素，若没有指定元素则报错
print(s2)
s2.pop()      # 默认删除hash表排列后的第一个元素
print(s2)
s2.discard(5)   # 删除指定元素，若没有指定元素则无事发生
print(s2)
```

## 交集&、并集 |

```python
s1={1,2,3}
s2={4,5,6}
s3={1,6}
print(s1 & s2)
print(s1 | s2)
print(s1 & s3)
print(s2 & s3)
```

# 可迭代对象的赋值

```py
li1=[1,2,3,4]
li2=li1
li1.append(5)
print(li1)
print(li2)
```

可迭代对象的赋值是给的地址，此时两个可迭代对象都会指向同一个地址(类似指针)，共享同一个地址的资源。当修改其中任意一个对象的值，即为修改该地址的值。此时所有共享该地址的可迭代对象都会发生改变。

# 深浅拷贝

## 浅拷贝

```python
li1=[1,2,3,4]
li2=li1
li1.append(5)
print('li1的地址：',id(li1))
print('li2的地址：',id(li2))
import copy
li3=[5,6,7,8,[9,10]]
li4=copy.copy(li3)  #浅拷贝，外层的地址不同，嵌套的内层地址相同，数据半共享
print('li3的地址：',id(li3))
print('li4的地址：',id(li4))
print('li3[4]的地址：',id(li3[4]))
print('li4[4]的地址：',id(li4[4]))
```

而为了保留原始数据，对其做出新的处理Python提供了copy模块。

copy方法可以只复制可迭代对象的值，而不指向该地址

## 深拷贝

```python
li1=[1,2,3,4]
li2=li1
li1.append(5)
print('li1的地址：',id(li1))
print('li2的地址：',id(li2))
import copy
li3=[5,6,7,8,[9,10]]
li4=copy.deepcopy(li3)  #深拷贝，外层地址不同，嵌套的内层地址也不同，数据完全不共享
print('li3[4]的地址：',id(li3[4]))
print('li4[4]的地址：',id(li4[4]))
```

# 可变类型和不可变类型

## 可变类型（list、dict、set）

变量对应的值可以修改，但是内存地址不会发生改变

```py
li=[1,2,3,4]
print('旧li的地址：',id(li))
li.append(5)
print('新li的地址：',id(li))
dic={'name':'ali','age':18}
print('旧dic的地址：',id(dic))
dic['name']="谢德萱"
print('新dic的地址：',id(dic))
set={1,2,3,4}
print('旧set的地址：',id(set))
set.remove(1)
print('新set的地址：',id(set))
```

## 不可变类型(int、str、tuple)

修改变量的值会重新生成一个新的值，将新值的地址给变量

```python
a=1
print(id(a))
a=2
print(id(a))
str="1234"
print(id(str))
str="2345"
print(id(str))
tua=(1,2,3,4)
print(id(tua))
tua=(2,3,4,5)
print(id(tua))
```

# 函数

## 位置参数

```python
def test(a):
    print("你是mvp！")
    return a;
print(test(100))
```

当有多个返回值的时候，返回值会以元组的形式被返回

```python
def test(a=12):   #设置参数的默认值，若调用函数时没有传递参数，则参数为默认值
    print("你是mvp！")
    return a;
print(test())
print(test(1))
```

## 可变参数

```python
def test(*args):  # 参数前加*代表是可变参数
    print(args)
    print(type(args))  # 可变参数是以元组形式传入函数的
test("谢德萱",'罗明珠')
print(type(test("李越",'黄灿'))) 
```

## 关键字参数

```python
def test(**kwargs):  # 参数前加**代表是可变参数
    print(kwargs)
    print(type(kwargs))  # 关键字参数是以字典形式传入函数的
test(first="谢德萱",second='罗明珠')
```

## 函数调用

```python
def MyBaby():
    print("我的宝贝是")
def test(**kwargs):
    MyBaby()
    print(kwargs)
    print(type(kwargs))
test(first="谢德萱",second='罗明珠')
```

## 函数嵌套

```python
def test(**kwargs):
    def MyBaby():
        print("我的宝贝是")
    MyBaby()
    print(kwargs)
    print(type(kwargs))
test(first="谢德萱",second='罗明珠')
```

## 在函数内部修改全局变量的值

```python
a=1
def test():
    global a  # 使用global关键字可以在函数内部修改全局变量的值
    a=100
    print(a)
test()
print(a)
```

```python
name='谢德萱'
age=20
cup='b'
height=160
def intro():
    global cup # 将cup声明为全局变量
    cup='A'
    print(f"我的名字是{name}，年龄是{age}，罩杯是{cup}，身高是{height}")
intro()
print(cup)
```

