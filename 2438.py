n = list(map(int, input("").split()))
n = [i*i for i in n]
print(sum(n)%10)