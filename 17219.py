import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()

n,m = map(int,input().split())
sites = {}
for _ in range(n):
    site_with_pw = input().split()
    sites[site_with_pw[0]] = site_with_pw[1]
for _ in range(m):
    print(sites[input()])