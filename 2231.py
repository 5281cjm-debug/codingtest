n = int(input(""))
strn = str(n)
deg = len(strn)
non = True
if deg > 2:
    for lower_n in range(n-deg*9,n):
        now_sum_n = lower_n
        for strn_one in str(lower_n):
            now_sum_n += int(strn_one)
        if now_sum_n == n:
            print(lower_n)
            non = False
            break
else:
    for lower_n in range(1,n):
        now_sum_n = lower_n
        for strn_one in str(lower_n):
            now_sum_n += int(strn_one)
        if now_sum_n == n:
            print(lower_n)
            non = False
            break
if non:
    print(0)