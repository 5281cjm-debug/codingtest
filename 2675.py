t=int(input(""))
for iter in range(t):
    r,s=input("").split()
    r = int(r)
    for chariter in s:
        print(chariter * r,end="")
    print()