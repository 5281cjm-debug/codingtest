n=input("")
ints = list(map(int,input("").split()))
sosu = True
sosu_cnt = 0
for int in ints:
    sosu = True
    if int < 2:
        continue
    for lower_int in range(2,int):
        if int%lower_int == 0:
            sosu = False
    if sosu:
        sosu_cnt += 1
print(sosu_cnt)
