# n = int(input(''))

# caled = 0
# while n > 1:
#     if n % 3 == 0 and n // 3 >= 1:
#         n = n//3
#         caled += 1
#     elif n % 4 == 0 and n // 2  >= 1 and (n // 2) % 3 != 0:
#         n = n//4
#         caled += 2

#     elif (n - 1) % 3 == 0 and (n - 1) // 3 >= 1:
#         n = n - 1
#         n = n // 3
#         caled += 2
#     elif n % 2 == 0 and n // 2 >= 1:
#         n = n//2
#         caled += 1
#     else:
#         n -= 1
#         caled += 1


# print(caled)

"""
n = int(input())
dp_n = [0,0]
for i in range(2,n+1):
    dp_n.append(dp_n[i-1] + 1)
    if i%2 == 0 and dp_n[i-1] > dp_n[i//2]:
        dp_n[i] = dp_n[i//2] + 1
    if i%3 == 0 and dp_n[i-1] > dp_n[i//3]:
        dp_n[i] = dp_n[i//3] + 1
print(dp_n[n])
"""

n = int(input())
dp_n = [0,0]
for i in range(2,n+1):
    dp_n.append(dp_n[i-1] + 1)
    if i%2 == 0 and dp_n[i] > dp_n[i//2] + 1:
        dp_n[i] = dp_n[i//2] + 1
    if i%3 == 0 and dp_n[i] > dp_n[i//3] + 1:
        dp_n[i] = dp_n[i//3] + 1
print(dp_n[n])