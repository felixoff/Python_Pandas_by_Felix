kol = int(input())
mas =[]
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    print(mas[i][0] + "," + mas[i][1] + ",", end="")
    if mas[i][2][0:6]=="Номер:":
        mas[i][2]=mas[i][2][6:]
    if mas[i][3].find(";",0,len(mas[i][3])) == -1:
        mas[i][3]= mas[i][3][:-1] + ";" + mas[i][3][-1:]
    print(mas[i][2] + "," + mas[i][3])
