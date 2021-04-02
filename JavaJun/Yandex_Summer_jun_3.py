kol = input().split(" ")
n = int(kol[0])
k = int(kol[1])
mas = (input().split(" "))
for i in range(n):
    mas[i] = int(mas[i])
answer = 0
for i in range(n):
    mas2 = mas.copy()
    del mas2[i]
    mas2.sort()
    flag = 0
    while (flag < k):
        list_of_difs = [abs(int(mas[i]) - int(x)) for x in mas2]
        result_index = list_of_difs.index(min(list_of_difs))
        a = mas2[result_index]
        answer = answer + abs(int(mas[i]) - int(a))
        del mas2[result_index]
        flag = flag + 1
    print(answer, end=" ")
    answer = 0