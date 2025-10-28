"""import sys
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    xy = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):
        x,y=map(int,input().split())
        xy[y][x] = 1
    for y in range(n):
        for x in range(m):
            if xy[y][x] == 1 and (x-1<0 or xy[y][x-1] != 1) and (y-1<0 or xy[y-1][x] != 1):
                count += 1
    print(count)"""

import sys
from collections import deque
def input():
    readin = sys.stdin.readline()
    return readin.rstrip()

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    xy = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        xy[y][x] = 1
    visited = set()
    count = 0
    for y in range(n):
        for x in range(m):      
            if (x,y) in visited:
                continue
            queue = deque()
            count += 1
            queue.append((x,y))
            while queue:
                w,h = queue.popleft()
                if w-1 >= 0 and xy[h][w-1] not in visited and xy[h][w-1] == 1:
                    queue.append((w-1,h))
                    visited.add((w-1,h))
                if w+1 < m and xy[h][w+1] not in visited and xy[h][w+1] == 1:
                    queue.append((w+1,h))
                    visited.add((w+1,h))
                if h-1 >= 0 and xy[h-1][w] not in visited and xy[h-1][w] == 1:
                    queue.append((w,h-1))
                    visited.add((w,h-1))
                if h+1 > n and xy[h+1][w] not in visited and xy[h+1][w] == 1:
                    queue.append((w,h+1))
                    visited.add((w,h+1))

    print(count)