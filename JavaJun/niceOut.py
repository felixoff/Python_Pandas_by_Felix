kol = int(input())
mas =[]
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    print("Номер бронирования " + mas[i][0] + ", " + "забронирован " +  mas[i][1] + ". " + "Цена: "+ mas[i][2][0:-3] + " руб. " +  mas[i][2][-2:] + " коп.")
