kol = int(input())
mas =[]
for i in range(kol):
    mas.append(input().split(","))
dict1 = {}
dict1["Scheduled"] = 0
dict1["On Time"] = 0
dict1["Delayed"] = 0
dict1["Departed"] = 0
dict1["Arrived"] = 0
dict1["Cancelled"] = 0
for i in range(kol):
    dict1[mas[i][1]] = dict1[mas[i][1]] + 1
for i in dict1.values():
    print(i)