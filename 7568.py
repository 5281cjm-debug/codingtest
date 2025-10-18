
def updown(x_ys, target, no_idx):
    weight_bools = []
    height_bools = []
    result_bools = []
    rate = 1
    for xy_idx, xy in enumerate(x_ys):
        if xy_idx == no_idx:
            continue
        if target[0] < xy[0]:
            weight_bools.append(True)
        else:
            weight_bools.append(False)
        
        if target[1] < xy[1]:
            height_bools.append(True)
        else:
            height_bools.append(False)
        
    for idx in range(len(height_bools)):
        if weight_bools[idx] and height_bools[idx]:
            result_bools.append(True)
        else:
            result_bools.append(False)
    for result_bool in result_bools:
        if result_bool:
            rate += 1
    return rate

n = int(input(''))
x_ys = []
xy_rates = []
for _ in range(n):
    x_ys.append(tuple(map(int,input('').split())))
for x_y_idx,x_y in enumerate(x_ys):
    xyrate = updown(x_ys, x_y, x_y_idx)
    xy_rates.append(xyrate)

for i in xy_rates:
    print(i,end=" ")