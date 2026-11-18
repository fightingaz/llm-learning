li1 = ["apple", "banana", "cherry", "watermelon", "grape"]
if not li1:
    print("清单为空")
for i in range(len(li1)):
    print(f"{i+1}. {li1[i]}")
for num,fruits in enumerate(li1,start=1):
    print(f"{num}. {fruits}")