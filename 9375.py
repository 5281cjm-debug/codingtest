import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()
def facto(num):
    result = 1
    while num > 1:
        result *=num
        num -= 1
    return result
def c(n,k):
    return facto(n)/(facto((n-k))*facto(k))

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        have_clothes = input().split()
        try:
            clothes[have_clothes[1]].append(have_clothes[0])
        except:
            clothes[have_clothes[1]] = (have_clothes[0])
    
    sets = 0
    fas_lens = []
    for fas in clothes.values():
        fas_lens.append(len(fas))
    for fas in range(len(clothes.keys())):
        c_n = c(len(clothes.keys()),fas)
        