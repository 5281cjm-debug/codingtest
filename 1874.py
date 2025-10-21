n = int(input())
want_num_list = []
for _ in range(n):
    want_num_list.append(int(input()))
to_stack_list = sorted(want_num_list)
stack = []
stacklog = []
for stack_num in to_stack_list:
    stack.append(stack_num)
    stacklog.append('+')
    try:
        while stack[-1] == want_num_list[0]:
            want_num_list.pop(0)
            stack.pop()
            stacklog.append('-')
    except IndexError:
        pass

if len(stack) != 0:
    print("NO")
else:
    for i in stacklog:
        print(i)