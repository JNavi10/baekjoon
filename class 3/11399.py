
def ATM():
    N = int(input())

    time_to_withdraw = list(map(int, input().split()))
    ttw_wait = []

    time_to_withdraw.sort()

    sum_time=0
    for i in range(N):
        sum_time += time_to_withdraw[i]
        ttw_wait.append(sum_time)

    print(sum(ttw_wait))



ATM()