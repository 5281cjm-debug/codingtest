import sys

input = sys.stdin.readline

def get_a_max(k,a):
    if k == 0:
        return 0
    max_a_i = 0
    for a_i in a:
        if a_i <= k:
            max_a_i = a_i
            break

    max_a_i_count = k // max_a_i
    left = k % max_a_i
    return max_a_i_count + get_a_max(left,a)


n,k = map(int,input().split())
a = []

for _ in range(n):
    a.append(int(input().rstrip()))
a.reverse()
print(get_a_max(k,a))