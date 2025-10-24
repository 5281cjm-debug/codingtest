import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        have_clothes = input().split()
        try:
            clothes[have_clothes[1]].append(have_clothes[0])
        except:
            clothes[have_clothes[1]] = (['no'])
            clothes[have_clothes[1]].append(have_clothes[0])

    sets = 1
    fas_lens = []
    for fas in clothes.values():
        fas_lens.append(len(fas))
    
    for i in fas_lens:
        sets *= i
    sets -= 1
    print(sets)
        