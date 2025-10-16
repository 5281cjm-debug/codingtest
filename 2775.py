t = int(input(""))

for _ in range(t):
    k = int(input(""))
    n = int(input(""))
    ns = [i for i in range(1,n+1)]
    for floor in range(k):
        nown = ns.copy()
        for ho_idx,ho in enumerate(ns):
            for hocnt in range(ho_idx):
                nown[ho_idx] += ns[hocnt]
        ns = nown
    print(ns[-1])