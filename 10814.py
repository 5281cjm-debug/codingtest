n = int(input(''))
cost_infos = []
for _ in range(n):
    age, name = input('').split()
    cost_infos.append((int(age), name))
cost_infos = sorted(cost_infos,key=lambda x: x[0])
for cost_info in cost_infos:
    print(cost_info[0],cost_info[1])