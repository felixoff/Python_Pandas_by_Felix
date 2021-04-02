def toxic(mas):
    for i in range(kol - 1):
        if (mas[i+1] < mas[i]):
            return(-1)
    itog = mas[len(mas)-1]-mas[0]
    return(itog)

kol = int(input())
mas = (input().split(" "))
for i in range(kol):
    mas[i] = int(mas[i])
itogo = toxic(mas)
print(itogo)