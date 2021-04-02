kol = int(input())
mas =[]
mas2=[]
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    mas2.append(mas[i][1])
for i, item in enumerate(mas2):
    mas2[i] = int(item)
mas2.sort()
from collections import Counter
count = Counter(mas2).most_common(1)[0][1]
new = Counter(mas2)
for key, value in new.items():
    if value == count:
        print(key, end=" ")



