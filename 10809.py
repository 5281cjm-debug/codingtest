alpas = {chr(i):-1 for i in range(97,123)}
s = input("")
for index, char in enumerate(s):
    if alpas[char] == -1:
        alpas[char] = index
for sit in alpas.values():
    print(sit,end=" ")