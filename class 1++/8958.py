test_case_count = int(input())

for _ in range(test_case_count):
    test_scores = str(input())
    total_score = 0
    conseq = 1
    while test_scores:
        if test_scores[0] == 'O':
            total_score += conseq
            conseq += 1
        else:
            conseq = 1
        test_scores = test_scores[1:]
        
    print(total_score)