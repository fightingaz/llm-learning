import json

menu = ["查看清单","添加待办","删除待办","退出"]
def show_menu():
    for k,v in enumerate(menu,start=1):
        print(f"{k}. {v}")
def load_todos(path="todos.json"):
    try:
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_todos(todos, path="todos.json"):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(todos,f,ensure_ascii=False,indent=2)
def show_todos(todos):
    if todos:
        for k,v in enumerate(todos,start=1):
            sta = "已完成" if v["完成"] else "未完成"
            print(f"{k}. {v['内容']} [{sta}]")
        print("---------------")
    else:
        print("清单为空！")
def add_todos(todos):
    print("请输入你想要添加的内容:")
    content = input()
    if content:
        todos.append({"内容": content, "完成": False})
        print("添加成功")
    else:
        print("内容为空,不予添加！")
    return todos
def del_todos(todos):
    if not todos:
        print("列表为空！")
        return todos
    else:
        print("请输入你想删除的事项编号：")
        try:
            index = int(input()) - 1
        except ValueError:
            print("请输入数字编号！")
            return todos
        if 0 <= index < len(todos):
            todos.pop(index)
            print("删除成功")
        else:
            print("编号越界，重新输入：")
        return todos
def main():
    todos = load_todos("todos.json")
    while True:
        show_menu()
        print("请输入你想进行的操作的编号：")
        try:
            todos_choice = int(input())
        except ValueError:
            print("请输入数字编号！")
            continue
        if todos_choice == 1:
            show_todos(todos)
        elif todos_choice == 2:
            todos = add_todos(todos)
            save_todos(todos,"todos.json")
        elif todos_choice == 3:
            show_todos(todos)
            del_todos(todos)
            save_todos(todos,"todos.json")
        elif todos_choice == 4:
            break
        else: print("没有这个选项,请重新输入")
main()