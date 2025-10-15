a,b=map(int,input("").split())
p = b-a
for i in range(p):
    if p % (i+1) == 0 and b % (i+1) == 0:
        b = b//(i+1)
        p = p//(i+1)
        
print(p,b)