p = 0
while True:
    try:
        i=input("")
        p+=1
    except EOFError:
        print(p)
        break