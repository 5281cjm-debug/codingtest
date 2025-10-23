import sys

input = sys.stdin.readline

n = int(input())
p = [(idx, (int(i))) for idx,i in enumerate(input().split())]


p = sorted(p,key=lambda x: x[1])

time = 0
total_time = 0
for pi in p:
    time += pi[1]
    total_time += time

print(total_time)