n = int(input(''))
x_ys = []

for _ in range(n):
    x_ys.append(tuple(map(int,input('').split())))

x_ys = sorted(x_ys,key=lambda x: (x[1],x[0]))
for i in x_ys:
    print(i[0],i[1])