import sys

input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    prompts = input().rstrip('\n')
    commends = prompts.split()
    if commends[0] == 'add':
        s.add(int(commends[1]))
    elif commends[0] == 'remove':
        try:
            s.remove(int(commends[1]))
        except:
            pass
    elif commends[0] == 'check':
        if int(commends[1]) in s:
            print(1)
        else:
            print(0)
    elif commends[0] == 'toggle':
        if int(commends[1]) in s:
            s.remove(int(commends[1]))
        else:
            s.add(int(commends[1]))
    elif commends[0] == 'all':
        s = set([i for i in range(1,21)])
    elif commends[0] == 'empty':
        s = set([])
