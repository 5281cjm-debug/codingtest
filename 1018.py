n,m = map(int,input('').split())

s = ''
for _ in range(n):
    s += input('')

fixed_s1 = ''
for h in range(8):
    for w in range(8):
        if (w+h) % 2 == 0:
            fixed_s1 += 'W'
        else:
            fixed_s1 += 'B'

start_n = 0
start_m = 0
eq_num = 0
while start_n + 8 <= n:
    for h in range(start_n,start_n+8):
        for w in range(start_m,start_m+8):
            

    if n*m - eq_num > eq_num:
        print(eq_num)
    else:
        print(n*m - eq_num)