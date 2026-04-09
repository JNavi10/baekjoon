test_case_count = int(input())

for _ in range(test_case_count):
    N, curious = map(int, input().split())
    Q = list(map(int, input().split()))

    count = 0
    def prioritize(Q, curious):
        while True:
            if Q[0] < max(Q):
                Q.append(Q.pop(0))
                curious -= 1
                if curious < 0:
                    curious += len(Q)
            else:
                break
        return Q, curious
    while Q:
        Q, curious = prioritize(Q, curious)
        #print('\t', Q, curious)
        Q.pop(0)
        curious -= 1
        count += 1
        if curious == -1:
            break
    print(count)
    