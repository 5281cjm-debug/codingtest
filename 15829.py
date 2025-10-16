l = int(input(""))
s = input("")
r = 31
m = 1234567891
inc = 0
total_s = 0
for char in s:
    dec = (ord(char)-96) * r**inc
    inc+=1
    total_s += dec
print(total_s%m)