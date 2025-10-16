while True:
    num = input("")
    if num == '0':
        break
    pal = True
    for ind in range(len(num)//2):
        if num[ind] != num[-ind-1]:
            pal = False
            break
            
    if pal:
        print("yes")
    else:
        print("no")