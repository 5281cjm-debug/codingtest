import sys
input = sys.stdin.readline

n = int(input())
numlist = []
for _ in range(n):
    new_num = int(input())
    idx = 0
    try:
        while numlist[idx] < new_num:
            idx+=1
        numlist.insert(idx,new_num)
    except:
        numlist.append(new_num)
for num in numlist:
    print(num)