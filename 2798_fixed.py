n, m = map(int, input().split())
cards = list(map(int, input().split()))

best = 0
for card1 in range(n-2):
    for card2 in range(card1+1, n-1):
        for card3 in range(card2+1, n):
            reg_total = cards[card1] + cards[card2] + cards[card3]
            if reg_total <= m and reg_total > best:
                best = reg_total
print(best)
#탐색~