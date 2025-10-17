n = int(input(""))
factorial_n = 1
for dn in range(n,0,-1):
    factorial_n *= dn
zeros = 0
for str_d_facto in reversed(str(factorial_n)):
    if str_d_facto == '0':
        zeros += 1
    else:
        break
print(zeros)