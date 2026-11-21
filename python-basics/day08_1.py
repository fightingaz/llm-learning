with open("notes.txt","w",encoding="utf-8") as f: # with ... as f: 是“用完自动关”的写法，离开缩进 f 自动 close()
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
with open("notes.txt","r",encoding="utf-8") as f:
    print(f.read())