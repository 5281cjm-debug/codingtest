for _ in range(int(input())):
    p = [1,1,1,2,2]
    n = int(input())
    while len(p)  < n:
        p.append(p[-1] + p[-5])
    print(p[n-1])