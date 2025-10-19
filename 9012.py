bal_strings_bool = []
for i in range(int(input(''))):
    string = input('')
    state = []
    unbal = False
    for abc in string:
        try:
            if abc == '(':
                state.append('(')
            elif abc == ')':
                if state[-1] != '(':
                    unbal = True
                    break
                else:
                    state.pop()
            elif abc == '[':
                state.append('[')
            elif abc == ']':
                if state[-1] != '[':
                    unbal = True
                    break
                else:
                    state.pop()
        except:
            unbal = True
    if len(state) != 0:
        unbal = True
    if unbal:
        bal_strings_bool.append(False)
    else:
        bal_strings_bool.append(True)

for bal_string_bool in bal_strings_bool:
    if bal_string_bool:
        print('YES')
    else:
        print('NO')
