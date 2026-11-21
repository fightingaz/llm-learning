import json

try:
    with open("todos.json","r",encoding="utf-8") as f:
        todos = json.load(f)
    todos.append({"内容": "上课","完成": False})
    # todos.pop(0)
except FileNotFoundError:
    todos = []
with open("todos.json","w",encoding="utf-8") as f:
    json.dump(todos,f,ensure_ascii=False,indent=2)
print(todos)