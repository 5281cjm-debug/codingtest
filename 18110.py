import sys

input = sys.stdin.readline
def round(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
n=int(input())
dificultys = []
for _ in range(n):
    dificultys.append(int(input()))
dificultys.sort()
del_rate = 30//2
del_num = round(len(dificultys) * del_rate / 100)
deleted_dificultys = dificultys[del_num:n - del_num]
if len(deleted_dificultys) == 0:
    print(0)
else:
    print(int(round(sum(deleted_dificultys)/len(deleted_dificultys))))