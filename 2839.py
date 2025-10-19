n = int(input(''))
bag_5_cnt = n//5
bag_3_cnt = 0
fiveandthree = False

while bag_5_cnt > 0:
    bag_3_cnt = 0
    bag_5_n = bag_5_cnt * 5
    while bag_5_n < n:
        bag_5_n += 3
        bag_3_cnt += 1
    if bag_5_n == n:
        fiveandthree = True
        break
    bag_5_cnt -= 1

if fiveandthree:
    print(bag_3_cnt+bag_5_cnt)
elif n % 3 == 0:
    print(n//3)
else:
    print(-1)
