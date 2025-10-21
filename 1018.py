n,m = map(int,input('').split())

s = []
for _ in range(n):
    s.append(input(''))


start_n = 0
start_m = 0
min_eq_num = 65

while start_n + 8 <= n:
    eq_num = 0
    for h in range(start_n,start_n+8):
        for w in range(start_m,start_m+8):
            if (h+w) % 2 == 0:
                if s[h][w] == 'W':
                    eq_num += 1
            else:
                if s[h][w] == 'B':
                    eq_num += 1
    if start_m+8 < m:
        start_m += 1
    else:
        start_m = 0
        start_n += 1

    min_eq_num = min(eq_num,64-eq_num,min_eq_num)
print(min_eq_num)