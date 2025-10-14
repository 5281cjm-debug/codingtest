n,x=map(int,input("").split())
a = list(map(int,input("").split()))
up = [i for i in a if i<x]
for i in up:
    print(i,end=" ")