kol = int(input())
mas =[]
dict1 = {}
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    if int(mas[i][1]) not in dict1:
        dict1[int(mas[i][1])] = []
    dict1[int(mas[i][1])].append(mas[i][3])
print(dict1)
for i in sorted(dict1):
    print(i)
    print(",".join(dict1[i]))
