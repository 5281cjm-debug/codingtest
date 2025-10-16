"""
0+1
6+1
18+1
36+1
60+1

0
1
3
6
10
"""
n = int(input(""))
inc = 1
mul = 0
while True:
    if 6*mul+1 >= n:
        break
    mul += inc
    inc += 1
print(inc)