a = input("")
b = input("")
c = input("")
d = 0
try:
    d = int(a) + 3
except:
    try:
        d = int(b) + 2
    except:
        d = int(c) + 1

if d%3 == 0 and d%5 == 0:
    print("FizzBuzz")
elif d%3 == 0:
    print("Fizz")
elif d%5 == 0:
    print("Buzz")
else:
    print(d)