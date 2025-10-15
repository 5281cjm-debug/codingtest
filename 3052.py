sets = set({})
for i in range(10):
    num = int(input(""))
    sets.add(num%42)
print(len(sets))