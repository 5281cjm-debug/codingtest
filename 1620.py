import sys

input = sys.stdin.readline

n,m = map(int,input().split())
pocketmons_num = {}
num_pocketmons = {}
for idx,_ in enumerate(range(n)):
    i = input().rstrip('\n')
    num_pocketmons[idx+1] = i
    pocketmons_num[i] = idx+1
for _ in range(m):
    i = input().rstrip('\n')
    try:
        i = int(i)
        print(num_pocketmons[i])
    except:
        print(pocketmons_num[i])