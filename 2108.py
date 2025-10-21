import sys



input = sys.stdin.readline
n=int(input())
nums={}
numlist=[]
num_sum = 0 #이거 딕셔너리 호출해가면서 또 다 더하면 시간초과될거같으니 미리 더해놓을 예정.
for _ in range(n):
    num = int(input())
    try:
        nums[num] += 1
    except:
        nums[num] = 1
    num_sum += num
    numlist.append(num)
mean = num_sum / sum(nums.values())
sort_num_keys = sorted(numlist)
middle = sort_num_keys[n//2] #sort_num_keys[len(sort_num_keys)//2]



most = sorted(nums.keys(),key=lambda x: (-nums[x],x))
try:
    if nums[most[0]] == nums[most[1]]:
        most = most[1]
    else:
        most = most[0]
except IndexError:
    most = most[0]
ranges = max(nums.keys()) - min(nums.keys())

print(int(round(mean,0)))
print(middle)
print(most)
print(ranges)