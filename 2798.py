import numpy as np
n,m = map(int,input("").split())
cards = np.array(list(map(int,input("").split())))
no_card12 = np.array([])

minsub = np.inf

for card1_idx, card1 in enumerate(cards):
    for card2_idx, card2 in enumerate(cards):
        if card1_idx == card2_idx:
            continue
        no_card12 = cards.copy()
        no_card12 = np.delete(no_card12,[card1_idx, card2_idx],axis=0)
        subedcards = no_card12 - (m-(card1+card2))
        try:
            reg_minsub = min(subedcards[subedcards*-1>=0]*-1)
            if reg_minsub < minsub:
                minsub = reg_minsub
        except:
            continue
print(m-minsub)