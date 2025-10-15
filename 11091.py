n = int(input(""))
for line in range(n):
    alpas = [chr(i) for i in range(97,123)]
    s = input("").lower()
    for char in s:
        if char in alpas:
            alpas.remove(char)
    if len(alpas) == 0:
        print("pangram")
    else:
        print("missing",end=" ")
        for missing in alpas:
            print(missing,end="")
        print()