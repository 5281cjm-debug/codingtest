n = int(input(""))
scores = list(map(int,input("").split()))
sum = 0
for score in scores:
    sum += score/max(scores)*100
result_mean = sum/len(scores)
print(result_mean)