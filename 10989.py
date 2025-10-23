# import sys
# input = sys.stdin.readline

# n = int(input())
# numlist = []
# for _ in range(n):
#     new_num = int(input())
#     try:
#         while numlist[idx] < new_num:
#             idx+=1
#         numlist.insert(idx,new_num)
#     except:
#         numlist.append(new_num)
# for num in numlist:
#     print(num)

import sys
input = sys.stdin.readline

n = int(input())
count_of_nums = [0 for _ in range(10001)]

for _ in range(n):
    new_num = int(input())
    count_of_nums[new_num] += 1

for idx,count_of_num in enumerate(count_of_nums):
    for _ in range(count_of_num):
        print(idx)