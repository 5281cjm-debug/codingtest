k = int(input(''))
stack = []
for _ in range(k):
    now_input = int(input(""))
    if now_input == 0:
        stack.pop()
    else:
        stack.append(now_input)
print(sum(stack))