max = 0
maxind = 0
for i in range(9):
    num = int(input(""))
    if num>max:
        max=num
        maxind = i+1
print(max)
print(maxind)