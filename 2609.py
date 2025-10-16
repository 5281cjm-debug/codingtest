#a,b=map(int,input("").split())
#yak = []
#for i in range(min(a,b),0,-1):
#    if a%i == 0 and b%i == 0:
#        yak.append(i)
#
a,b=map(int,input("").split())
ayak = set([])
byak = set([])
for ainc in range(1,a+1):
    if a%ainc == 0:
        ayak.add(ainc)
for binc in range(1,b+1):
    if b%binc == 0:
        byak.add(binc)
sameyaks = ayak & byak
maxsameyak = max(sameyaks)
minsamebe = maxsameyak * a//maxsameyak * b//maxsameyak
print(maxsameyak)
print(minsamebe)