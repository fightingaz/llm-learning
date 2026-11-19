menu = ["查看清单","添加待办","删除待办","退出"]
todos = []
while True:
    print("=====待办清单=====")
    for num1,thing1 in enumerate(menu, start=1):
        print(f"{num1}. {thing1}")
    print("请选择操作：")
    try:
        op = int(input())
    except ValueError:
        print("请输入数字！")
        continue
    if op == 1:
        if not todos:
            print("清单为空！")
        else:
            for num2,thing2 in enumerate(todos, start=1):
                print(f"{num2}. {thing2}")
    elif op == 2:
        print("输入你的待办事项：")
        want = input()
        if not want:
            print("内容不能为空！")
        else:
            todos.append(want)
            print("添加成功！")
    elif op == 3:
        if todos:
            for num2, thing2 in enumerate(todos, start=1):
                print(f"{num2}. {thing2}")
            print("输入你想删除待办事项的编号：")
            try:
                d = int(input())
            except ValueError:
                print("请输入数字！")
                continue
            if 0 < d <= len(todos):
                todos.pop(d - 1)
                print("删除成功")
            else:
                print("编号不存在,请重新输入：")
        else:
            print("清单为空！")
    elif op == 4:
        break
    else:
        print("没有这个选项！")

