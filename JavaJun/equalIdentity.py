kol = int(input())
mas =[]
dict1 = {}
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    for j in range(len(mas[i])):
        if int(mas[i][j]) not in dict1:
            dict1[int(mas[i][j])] = 0
        dict1[int(mas[i][j])] = dict1[int(mas[i][j])]  + 1
for i in sorted(dict1):
    if (dict1[i] < 2):
        del dict1[i]
mas2 =[]
for i in sorted(dict1.keys()):
    mas2.append(i)
for i in range(len(mas2)-1):
    print(mas2[i],end = ",")
if (len(mas2) > 0):
    print(mas2[len(mas2)-1])

