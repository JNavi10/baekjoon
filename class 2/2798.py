N, M = map(int, input().split())

li = list(map(int, input().split()))
ans = 0

def brute_force(sum: int, lis:list, n_count: int):
    global ans
    print(sum, lis, n_count)
    if n_count == 1:
        for i in lis:
            temp = sum + i
            print(temp)
            if abs(ans-M) > abs(temp-M):
                print('temp update')
                ans = temp
    else:
        brute_force(sum + lis[0], lis[1:], n_count-1)
for i in range(len(li)):
    li.pop(i)
    brute_force(0, li.copy(), 3)
print(ans)