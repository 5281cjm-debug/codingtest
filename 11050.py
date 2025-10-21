# def facto(num):
#     if num == 1:
#         return 1
#     return num * facto(num-1)

def facto(num):
    result = 1
    while num > 1:
        result *=num
        num -= 1
    return result
def c(n,k):
    return facto(n)/(facto((n-k))*facto(k))
n,k=map(int,input().split())
print(int(c(n,k)))
