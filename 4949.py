# bal_strings_bool = []
# while True:
#     string = input('')
#     if string == '.':
#         break
#     finding_l = []
#     finding_b = []
#     state = []
#     unbal = False
#     for abc in string:
#         if abc == '(':
#             finding_l.append(True)
#         elif abc == ')':
#             if len(finding_l) == 0:
#                 unbal = True
#                 break
#             else:
#                 finding_l.pop()
#         elif abc == '[':
#             finding_b.append(True)
#         elif abc == ']':
#             if len(finding_b) == 0:
#                 unbal = True
#                 break
#             else:
#                 finding_b.pop()
#     if len(finding_l) != 0 or len(finding_b) != 0:
#         unbal = True
#     if unbal:
#         bal_strings_bool.append(False)
#     else:
#         bal_strings_bool.append(True)

# for bal_string_bool in bal_strings_bool:
#     print(bal_string_bool)

bal_strings_bool = []
while True:
    string = input('')
    if string == '.':
        break
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
        print('yes')
    else:
        print('no')
