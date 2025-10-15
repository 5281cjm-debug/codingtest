t = int(input(""))
for case in range(t):
    h,w,n = map(int,input("").split())
    if n%h == 0:
        ch = h
        cw = n//h
    else:
        cw = n//h+1
        ch = n%h
    print(f"{ch}{cw:02d}")