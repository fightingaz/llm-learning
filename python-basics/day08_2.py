import json

todos = [
    {"内容": "买菜","完成": False},
    {"内容": "写代码","完成": True},
]

with open("todos.json","w",encoding="utf-8") as f:
    json.dump(todos,f,ensure_ascii=False,indent=2)
with open("todos.json","r",encoding="utf-8") as f:
    todos = json.load(f)
print(todos)
todos.append({"内容": "洗澡","完成": False})

with open("todos.json","w",encoding="utf-8") as f:
    json.dump(todos,f,ensure_ascii=False,indent=2)
print(todos)