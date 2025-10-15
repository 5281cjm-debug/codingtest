n = int(input(""))
sizes = list(map(int,input("").split()))
t,p=map(int,input("").split())
#S,M,L,XL,XXL,XXXL
pack_cnt = 0

for size in sizes:
    if size%t==0:
        pack_cnt+=size//t
    else:
        pack_cnt+=size//t+1
print(pack_cnt)
print(n//p,n%p)