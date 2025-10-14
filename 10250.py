t = int(input(""))
for case in range(t):
    h,w,n = map(int,input("").split())
    cw = str(n//h+1)
    ch = str(n%h)
    print(ch+"0"+cw)