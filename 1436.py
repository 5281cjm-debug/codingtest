n = int(input(''))
cnt = 0
while True:
    cnt+=1
    for num_idx, num in enumerate(str(cnt)[:-2]):
        if num == '6':
            if str(cnt)[num_idx+1] == '6' and str(cnt)[num_idx+2] == '6':
                n-=1
                break
    if n == 0:
        break

print(cnt)