

def solve_new_min_max(new_arr = [1,2,3], old_arr = [4,5,6]):
    solved_min_arr: list[int] = []
    solved_max_arr = []
    # j는  새 arr의 index
    for j in range(3):
        new_min: int = 0
        new_max = 0
        min_first_iter = True
        max_first_iter = True
        # k는 구 arr의 index
        for k in range(3):
            # index 차이 2 이상이면 skip
            if abs(j-k) >= 2:
                continue
            # print(j,k)
            # 각 j 와 가능한 k 값 결합
            #print(f"new_arr[{j}]={new_arr[j]}, old_arr[{k}]={old_arr[k]}")
            new_min_j_k: int = new_arr[j] + old_arr[k]
            # arr값 임시 갱신
            if new_min > new_min_j_k or min_first_iter:
                new_min = new_min_j_k
                min_first_iter = False
            if new_max < new_min_j_k or max_first_iter:
                new_max = new_min_j_k
                max_first_iter = False
        # arr값 영구 갱신
        # print(f'min for {j} is {new_min}')
        solved_min_arr.append(new_min)
        #print(f'max for {j} is {new_max}')
        solved_max_arr.append(new_max)

    return solved_min_arr, solved_max_arr

"""
arr1 = [2, 0, 0]
arr2 = [4 ,1, 1]
arr3 = [1, 2, 6]
max_state = arr1
#min_state, _ = solve_new_min_max(input_arr, min_state)
_, max_state = solve_new_min_max(arr2, max_state)
print(max_state) # 6, 2, 1
_, max_state = solve_new_min_max(arr3, max_state)
print(max_state) # 7, 8, 8
#print(solve_new_min_max())


exit(123)
"""

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

    min_state, _ = solve_new_min_max(input_arr, min_state)
    _, max_state = solve_new_min_max(input_arr, max_state)

    

print(max(max_state), min(min_state))