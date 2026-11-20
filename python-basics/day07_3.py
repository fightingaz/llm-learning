todos = []

for i in range(2):
    want = input()
    todos.append({"内容": want, "完成": False})
for k,v in enumerate(todos,start=1):
    status = "已完成" if v["完成"] else "未完成"
    print(f"{k}. {v['内容']} [{status}]")