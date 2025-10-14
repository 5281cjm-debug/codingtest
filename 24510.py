C = int(input(""))
max = 0
for i in range(C):
    line = input("")
    linemax = 0
    for ind, s in enumerate(line):
        if s=='f' and ind != len(line)-2:
            if line[ind:ind+3] == 'for':
                linemax+=1
        if s=='w' and ind != len(line)-4:
            if line[ind:ind+5] == 'while':
                linemax+=1
    if linemax > max:
        max = linemax
print(max)