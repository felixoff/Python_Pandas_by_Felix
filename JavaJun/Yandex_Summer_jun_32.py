from time import time
tic = time()
def get_answer(n,k,mas):
    for i in range(n):
        answer = 0
        mas2 = mas.copy()
        del mas2[i]
        mas2.sort()
        q = int(mas[i])
        list_of_difs = [abs(q - int(x)) for x in mas2]
        for flag in range(k):
            result_index = list_of_difs.index(min(list_of_difs))
            a = mas2[result_index]
            answer = answer + abs(q - int(a))
            del list_of_difs[result_index]
            del mas2[result_index]
        print(answer, end=" ")

kol = input().split(" ")
n = int(kol[0])
k = int(kol[1])
mas = (input().split(" "))
get_answer(n,k,mas)
toc = time()
print(toc - tic)
