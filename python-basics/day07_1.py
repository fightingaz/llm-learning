# 学生信息卡
dic = {"name":"xbw","age": 0,"major":"cs"}
dic["age"] = 23
dic["graduated"] = False
for k,v in dic.items():
    print(f"{k}: {v}")
print(dic.get("name"))