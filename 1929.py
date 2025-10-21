"""m,n = map(int,input('').split())
sosus = []
insosu = False
for i in range(m,n+1):
    if i == 1:
        continue
    i_sosu = True
    if insosu:
        for o in sosus+list(range(sosus[-1],i//2+1)):
            if i%o == 0:
                i_sosu = False
                break
        if i_sosu:
            sosus.append(i)
    else:
        for o in range(m,i//2+1):
            if i%o == 0:
                i_sosu = False
                insosu=True
                break
        if i_sosu:
            sosus.append(i)
strsosus = []
for i in sosus:
    strsosus.append(str(i))
print('\n'.join(strsosus))
"""

m,n = map(int,input('').split())

for i in range(m,n+1):
    issosu = True
    if i == 1:
        continue
    for o in range(2,int(i**0.5)+1):
        if i%o == 0:
            issosu = False
            break
    if issosu:
        print(i)