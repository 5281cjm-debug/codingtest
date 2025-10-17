a,b,v = map(int,input("").split())
uplen = a
dayup = a-b
if (v-a) % dayup == 0:
    day = 1 + (v-a) // dayup
else:
    day = 1 + (v-a) // dayup + 1
print(day)