n = int(input(""))
words = []
for _ in range(n):
    words.append(input(""))
words = list(set(words))
words = sorted(words) # 알파벳순 정렬
words = sorted(words, key = lambda x : (len(x))) # 길이순 정렬
for word in words:
    print(word)