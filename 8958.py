n = int(input(""))
for iter in range(n):
    test_result = input("")
    correct = 0
    score = 1
    for question_result in test_result:
        if question_result == 'O':
            correct += score
            score += 1
        else:
            score = 1
    print(correct)