import datetime

kol = int(input())
mas =[]
for i in range(kol):
    mas.append(input().split(","))
for i in range(kol):
    date_time_obj = datetime.datetime.strptime(mas[i][0], '%Y-%m-%dT%H:%M')
    date_time_obj2 = datetime.datetime.strptime(mas[i][2], '%Y-%m-%dT%H:%M')
    date_time_obj3 = datetime.datetime.strptime(mas[i][1], '%Y-%m-%dT%H:%M')
    date_time_obj4 = datetime.datetime.strptime(mas[i][3], '%Y-%m-%dT%H:%M')
    if (abs((date_time_obj2-date_time_obj).seconds) < 1800 or abs((date_time_obj-date_time_obj2).seconds) <1800)\
            and (abs((date_time_obj4-date_time_obj3).seconds) < 1800 or abs((date_time_obj3-date_time_obj4).seconds) <1800)\
            :
        print("YES")
    else:
        print("NO")