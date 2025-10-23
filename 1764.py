import sys

input = sys.stdin.readline

n,m = map(int,input().split())
dj = set({})
bj = set({})
for _ in range(n):
    i = input().rstrip('\n')
    dj.add(i)
for _ in range(m):
    i = input().rstrip('\n')
    bj.add(i)
dbj = dj & bj

print(len(dbj))
list_dbj = sorted(list(dbj))
for i in list_dbj:
    print(i)