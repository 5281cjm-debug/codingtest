while True:
    s1,s2,s3 = map(int,input("").split())
    if s1 == s2 == s3 == 0:
        break
    sorted_s = sorted([s1,s2,s3])
        
    if sorted_s[0]**2 + sorted_s[1]**2 == sorted_s[2]**2:
        print("right")
    else:
        print("wrong")