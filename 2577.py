a=int(input(""))
b=int(input(""))
c=int(input(""))
result = a*b*c

l = {str(i):0 for i in range(10)}
for num in str(result):
    l[num]+=1
for val in l.values():
    print(val)
