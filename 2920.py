ints = list(map(int,input("").split()))
ascend = list(range(1,9))
descend = list(range(8,0,-1))
if ints == ascend:
    print("ascending")
elif ints == descend:
    print("descending")
else:
    print("mixed")