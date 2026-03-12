

def solve_new_min_max(new_arr:list[int], old_arr:list[int]):
    # 결과 배열: 연산 결과가 저장될 min 배열과 max 배열
    solved_min_arr = []
    solved_max_arr = []

    # j는 새 배열의 index
    for j in range(3):
        # 새 결과 배열에 들어갈
        new_min = 0
        new_max = 0

        # 첫번째 결과값은 무조건 저장하기 위한 첫번째 결과값 식별 변수
        min_first_iter = True
        max_first_iter = True

        # k는 구 배열의 index
        for k in range(3):
            # index 차이 2 이상이면 skip -, j,k: (0, 2), (2, 0) 걸러냄
            if abs(j-k) >= 2:
                continue
            
            new_min_j_k: int = new_arr[j] + old_arr[k]

            # min, max 값만 필요하므로 값만 갱신
            if new_min > new_min_j_k or min_first_iter:
                new_min = new_min_j_k
                min_first_iter = False
            if new_max < new_min_j_k or max_first_iter:
                new_max = new_min_j_k
                max_first_iter = False

        # 각 j 별로 계산한 값을 결과 배열에 저장
        solved_min_arr.append(new_min)
        solved_max_arr.append(new_max)

    return solved_min_arr, solved_max_arr


N = int(input())

# i 는 입력 arr의 i번째 줄
for i in range(N):
    if i == 0: # 첫 줄은 그냥 카피
        input_arr = [int(x) for x in input().split()]
        min_state = input_arr.copy()
        max_state = input_arr.copy()
        continue
    
    # 새 줄 읽기
    input_arr = [int(x) for x in input().split()]

    # min 과 max 배열은 계산 대상이 다르므로 따로 계산
    min_state, _ = solve_new_min_max(input_arr, min_state)
    _, max_state = solve_new_min_max(input_arr, max_state)

print(max(max_state), min(min_state))