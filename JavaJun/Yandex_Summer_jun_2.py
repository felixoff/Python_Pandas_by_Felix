kol_rows = int(input())
mas_rows = []
for i in range(kol_rows):
    mas_rows.append(input())
kol_group = int(input())
mas_group = []
for i in range(kol_group):
    mas_group.append(input().split(" "))
for i in range(kol_group):
    flag = 0
    if (mas_group[i][1] == "left"):
        for j in range(kol_rows):
            if (mas_group[i][2] == "aisle" and mas_rows[j][0] == "." or
                    mas_group[i][2] == "window" and mas_rows[j][2:3].find(".") != -1):
                if mas_group[i][0] == "1" and mas_rows[j][0:3].find(".") != -1:
                    if (mas_group[i][2] == "aisle"):
                        a = 2
                    elif (mas_group[i][2] == "window"):
                        a = 0
                    else:
                        break
                    print("Passengers can take seats: " + str(j+1) + str(chr(a +65)))
                    mas_rows[j] = mas_rows[j][:a]+"X"+ mas_rows[j][a+1:]
                    for o in range(kol_rows):
                        print(mas_rows[o])
                    mas_rows[j] = mas_rows[j][:a]+"#"+ mas_rows[j][a+1:]
                    flag = 1
                    break
                elif mas_group[i][0] == "2" and mas_rows[j][0:3].find("..") != -1:
                    if (mas_group[i][2] == "aisle"):
                        a = 1
                    elif (mas_group[i][2] == "window"):
                        a = 0
                    else:
                        break
                    print('Passengers can take seats: ' + str(j+1) + str(chr(a+65)) + " "
                          + str(j+1) + str(chr(a + 1+65)))
                    mas_rows[j] = mas_rows[j][:a]+"XX"+ mas_rows[j][a+2:]
                    for o in range(kol_rows):
                        print(mas_rows[o])
                    mas_rows[j] = mas_rows[j][0:a]+"##"+ mas_rows[j][a+2:]
                    flag = 1
                    break
                elif mas_group[i][0] == "3" and mas_rows[j][0:3].find("...") != -1:
                    if (mas_group[i][2] == "aisle"):
                        a = 0
                    elif (mas_group[i][2] == "window"):
                        a = 0
                    else:
                        break
                    print("Passengers can take seats: " + str(j+1) + str(chr(a +65)) + " "
                          + str(j+1) + str(chr(a + 1+65)) + " "
                          + str(j+1) + str(chr(a + 2+65)))
                    mas_rows[j] = mas_rows[j][:a]+"XXX"+ mas_rows[j][a+3:]
                    for o in range(kol_rows):
                        print(mas_rows[o])
                    mas_rows[j] = mas_rows[j][:a]+"###"+ mas_rows[j][a+3:]
                    flag = 1
                    break
    elif (mas_group[i][1] == "right"):
        for j in range(kol_rows):
            if (mas_group[i][2] == "aisle" and mas_rows[j][4] == "." or
                    mas_group[i][2] == "window" and mas_rows[j][6:].find(".") != -1):
                if mas_group[i][0] == "1" and mas_rows[j][4:].find(".") != -1:
                    if (mas_group[i][2] == "aisle"):
                        a = 4
                    elif (mas_group[i][2] == "window"):
                        a = 6
                    else:
                        break
                    print("Passengers can take seats: " + str(j+1) + str(chr(a +64)))
                    mas_rows[j] = mas_rows[j][:a]+"X"+ mas_rows[j][a+1:]
                    for o in range(kol_rows):
                        print(mas_rows[o])
                    mas_rows[j] = mas_rows[j][:a]+"#"+ mas_rows[j][a+1:]
                    flag = 1
                    break
                elif mas_group[i][0] == "2" and mas_rows[j][4:].find("..") != -1:
                    if (mas_group[i][2] == "aisle"):
                        a = 4
                    elif (mas_group[i][2] == "window"):
                        a = 5
                    else:
                        break
                    print("Passengers can take seats: " + str(j+1) + str(chr(a +64)) + " "
                          + str(j+1) + str(chr(a + 1+64)))
                    mas_rows[j] = mas_rows[j][:a]+"XX"+ mas_rows[j][a+2:]
                    for o in range(kol_rows):
                        print(mas_rows[o])
                    mas_rows[j] = mas_rows[j][:a]+"##"+ mas_rows[j][a+2:]
                    flag = 1
                    break
                elif mas_group[i][0] == "3" and mas_rows[j][4:].find("...") != -1:
                    if (mas_group[i][2] == "aisle"):
                        a = 4
                    elif (mas_group[i][2] == "window"):
                        a = 4
                    else:
                        break
                    print("Passengers can take seats: " + str(j+1) + str(chr(a +64)) + " "
                          + str(j+1) + str(chr(a + 1+64)) + " "
                          + str(j+1) + str(chr(a + 2+64)))
                    mas_rows[j] = mas_rows[j][:a]+"XXX"+ mas_rows[j][a+3:]
                    for o in range(kol_rows):
                        print(mas_rows[o])
                    mas_rows[j] = mas_rows[j][:a]+"###"+ mas_rows[j][a+3:]
                    flag = 1
                    break
    if (flag == 0):
        print("Cannot fulfill passengers requirements")