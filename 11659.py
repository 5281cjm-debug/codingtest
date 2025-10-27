import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()

n,m=map(int,input().split())
ns = list(map(int,input().split()))
sumlist = [0]
for idx in range(len(ns)):
    sumlist.append(ns[idx] + sumlist[idx])
for _ in range(m):
    m1,m2 = map(int,input().split())
    print(sumlist[m2] - sumlist[m1-1])