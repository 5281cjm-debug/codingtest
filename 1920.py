n = int(input(""))
a = []
a = set(map(int,input('').split()))

m = int(input(""))
isa = []
isa = list(map(int,input('').split()))

for findnum in isa:
    if findnum in a:
        print(1)
    else:
        print(0)
