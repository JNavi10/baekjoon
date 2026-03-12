# min

arr_a = [1,2,3]
arr_b = [4,5,6]

# j는  새 arr의 index
for j in range(3):
    new_min = 0
    new_max = 0
    first_iter = True
    # k는 구 arr의 index
    for k in range(3):
        # index 차이 2 이상이면 skip
        if abs(j-k) >= 2:
            continue
        print(j,k)
        # 각 j 와 가능한 k 값 결합
        new_min_j_k = arr_b[j] + arr_a[k]
        # arr값 임시 갱신
        if new_min > new_min_j_k or first_iter:
            new_min = new_min_j_k
            first_iter = False
    # arr값 영구 갱신
    print(f'min for {j} is {new_min}')

exit(123)


N = int(input())

sum = 0

min_state = [0, 0, 0]
max_state = [0, 0, 0]

# i 는 입력 arr의 i번째 줄
for i in range(N):
    if i == 0: # 첫 줄은 그냥 카피
        input_arr = [int(x) for x in input().split()]
        min_state = input_arr.copy()
        max_state = input_arr.copy()
        continue
    
    # 새 input
    input_arr = [int(x) for x in input().split()]

    new_min_state = min_state.copy()
    new_max_state = max_state.copy()

    # j는  새 arr의 index
    for j in range(3):
        new_min = 0
        new_max = 0
        min_first_iter = True
        max_first_iter = False
        # k는 구 arr의 index
        for k in range(3):
            # index 차이 2 이상이면 skip
            if abs(j-k) >= 2:
                continue
            # 각 j 와 가능한 k 값 결합
            new_min_j_k = input_arr[j] + min_state[k]
            new_max_j_k = input_arr[j] + min_state[k]
            # arr값 임시 갱신
            if new_min > new_min_j_k or min_first_iter:
                new_min = new_min_j_k
                min_first_iter = False
            if new_max < new_max_j_k or max_first_iter:
                new_max = new_max_j_k
                max_first_iter = False
        # arr값 영구 갱신
        new_min_state[j] = new_min
        new_max_state[j] = new_max

    min_state = new_min_state.copy()
    max_state = new_max_state.copy()
    

print(max(max_state), min(min_state))