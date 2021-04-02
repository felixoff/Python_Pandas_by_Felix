kol = int(input())
mas =[]
mas2=[]
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    index = 0
    for j in range(i):
        if mas[j][0] == mas[i][0] and mas[j][1] == mas[j][1]:
            index = index + 1
    if index == 0:
        print(mas[i][0] + "," + mas[i][1] + ","+ mas[i][2] + "," + mas[i][3])

