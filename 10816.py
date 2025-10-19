n = int(input(''))
cards = list(map(int,input('').split()))
m = int(input(''))
find_cards = list(map(int,input('').split()))
carddict = {}
for card in cards:
    try:
        carddict[card] += 1
    except:
        carddict[card] = 1

for find_card in find_cards:
    try:
        print(carddict[find_card],end=' ')
    except:
        print(0,end=' ')