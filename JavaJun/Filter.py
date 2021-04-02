cond = input().split(",")
kol = int(input())
mas =[]
mas2=[]
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    for j in range(len(cond)):
        if (mas[i][1] == cond[j]):
            print(mas[i][0]+","+mas[i][1]+","+mas[i][2]+","+mas[i][3])